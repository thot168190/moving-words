import gradio as gr
import torch
from diffusers import AutoPipelineForText2Image

try:
    import spaces
except ImportError:
    # spaces 모듈이 없는 로컬 개발 환경용 가짜 데코레이터 선언
    class spaces:
        @staticmethod
        def GPU(*args, **kwargs):
            if args and callable(args[0]):
                return args[0]
            return lambda func: func


# 외부 Inference Provider를 다시 호출하지 않고 Space에 배정된 무료 GPU에서 직접 생성합니다.
# SDXL Turbo는 4단계만으로 생성되어 ZeroGPU 사용 시간을 줄일 수 있습니다.
MODEL_ID = "stabilityai/sdxl-turbo"
pipeline = None

STYLE_GUIDES = {
    "세밀 수채화": "delicate museum-quality watercolor, refined fine-line details",
    "잉크 드로잉": "sophisticated fine ink drawing with restrained watercolor accents",
    "빈티지 도감": "elegant vintage natural-history plate, archival illustration",
    "밝은 파스텔": "refined luminous pastel illustration, soft yet not childish",
    "귀여운 3D 점토": "adorable 3D claymation style, cute clay figure, soft plasticine illustration, warm whimsical lighting",
    "따뜻한 그림책": "whimsical storybook illustration, cozy children's book art style, soft crayon texture, endearing and magical",
}


def get_pipeline():
    """첫 요청에서 한 번만 모델을 올리고 이후 요청에서는 재사용합니다."""
    global pipeline
    if pipeline is None:
        pipeline = AutoPipelineForText2Image.from_pretrained(
            MODEL_ID,
            torch_dtype=torch.float16,
            variant="fp16",
            use_safetensors=True,
        )
        pipeline.to("cuda")
        pipeline.enable_attention_slicing()
    return pipeline


@spaces.GPU(duration=60)
def generate_card(word: str, meaning: str, scene: str, style: str):
    """텍스트가 없는 순백 배경 원화를 만듭니다. 단어 표기는 웹에서 정확히 얹습니다."""
    word = (word or "").strip()
    meaning = (meaning or "").strip()
    scene = (scene or "").strip()

    # 영단어나 한글 뜻 중 하나만 입력해도 정상 동작하도록 가드 완화
    if not word and not meaning:
        raise gr.Error("영어 단어 또는 한글 뜻 중 최소 하나는 입력해야 합니다.")

    style_guide = STYLE_GUIDES.get(style, STYLE_GUIDES["세밀 수채화"])

    # 아동용/동화용 친화 스타일일 때는 'no childish cartoon style' 가드 완화
    child_friendly = style in ["귀여운 3D 점토", "따뜻한 그림책"]
    cartoon_guard = "" if child_friendly else ", no childish cartoon style"

    prompt = f"""
    Create this exact scene: {scene or f'a clear visual representation of {word}'}.
    The main learning subject is the subject '{word if word else meaning}'
    ({meaning or 'vocabulary learning card'}). Use {style_guide}.
    Sophisticated educational editorial illustration for teenagers, centered and fully visible,
    balanced negative space, pure bright white background, crisp silhouette, elegant restrained colors,
    no text, no letters, no watermark, no frame, no hand{cartoon_guard}.
    """
    try:
        result = get_pipeline()(
            prompt=prompt,
            num_inference_steps=4,
            guidance_scale=0.0,
            width=768,
            height=768,
        )
        return result.images[0]
    except Exception as error:
        # 웹 화면에 의미 없는 null 대신 실제 원인을 전달합니다.
        raise gr.Error(f"이미지 생성 서버 오류: {error}") from error


with gr.Blocks(title="InkWord Image Lab") as demo:
    gr.Markdown("# 보는 단어장 · 내가 만드는 그림 단어")
    with gr.Row():
        word_input = gr.Textbox(label="영어 단어", placeholder="예: telescope (선택 입력)")
        meaning_input = gr.Textbox(label="한국어 뜻", placeholder="예: 망원경 (선택 입력)")
    scene_input = gr.Textbox(
        label="만들고 싶은 장면",
        placeholder="예: 별빛 아래 언덕 위에 놓인 망원경, 멀리 은하수가 보이게",
        lines=3,
    )
    style_input = gr.Radio(list(STYLE_GUIDES), value="세밀 수채화", label="그림 스타일")
    generate_button = gr.Button("그림 만들기", variant="primary")
    output_image = gr.Image(label="완성된 원화", type="pil")
    generate_button.click(
        generate_card,
        inputs=[word_input, meaning_input, scene_input, style_input],
        outputs=output_image,
        api_name="generate_card",
    )


if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        ssr_mode=False
    )
