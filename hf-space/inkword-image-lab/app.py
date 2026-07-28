import os

import gradio as gr
from huggingface_hub import InferenceClient
from gradio_client import Client

try:
    import spaces
except ImportError:
    # spaces 모듈이 없는 로컬 개발 환경용 가짜 데코레이터 선언
    class spaces:
        @staticmethod
        def GPU(func):
            return func


MODEL_ID = os.getenv("MODEL_ID", "stabilityai/stable-diffusion-xl-base-1.0")
client = InferenceClient(token=os.getenv("HF_TOKEN"))

STYLE_GUIDES = {
    "세밀 수채화": "delicate museum-quality watercolor, refined fine-line details",
    "잉크 드로잉": "sophisticated fine ink drawing with restrained watercolor accents",
    "빈티지 도감": "elegant vintage natural-history plate, archival illustration",
    "밝은 파스텔": "refined luminous pastel illustration, soft yet not childish",
    "귀여운 3D 점토": "adorable 3D claymation style, cute clay figure, soft plasticine illustration, warm whimsical lighting",
    "따뜻한 그림책": "whimsical storybook illustration, cozy children's book art style, soft crayon texture, endearing and magical",
}


def mentor_scene(word: str, meaning: str, scene: str) -> str:
    """사용자가 입력한 한글 장면 묘사를 AI가 이미지 생성을 위한 고품격 영어 프롬프트로 다듬고 멘토링합니다."""
    word = (word or "").strip()
    meaning = (meaning or "").strip()
    scene = (scene or "").strip()
    
    # 둘 중 입력이 들어온 단어를 기준 핵심 주체로 사용
    subject = word if word else meaning
    
    if not scene:
        return f"a clear visual representation of the subject '{subject}'"

    system_prompt = (
        "You are an expert English learning mentor and illustration art director.\n"
        "Your task is to translate the user's Korean description into a highly detailed, professional English image prompt.\n"
        "The goal is to create a clear, beautiful educational illustration for a vocabulary card representing the subject '{subject}' (English word: '{word}', Korean meaning: '{meaning}').\n"
        "Convert the description into a single, coherent English descriptive paragraph focusing on composition, lighting, style, and clarity.\n"
        "Do NOT include any conversational text, explanations, or metadata. Output ONLY the refined English prompt."
    )
    
    messages = [
        {"role": "system", "content": system_prompt.format(subject=subject, word=word, meaning=meaning)},
        {"role": "user", "content": f"Korean scene description: {scene}"}
    ]
    
    try:
        response = client.chat_completion(
            messages=messages,
            model="meta-llama/Llama-3.1-8B-Instruct",
            max_tokens=256,
            temperature=0.7
        )
        refined = response.choices[0].message.content.strip()
        # 불필요한 감싸인 따옴표 제거
        refined = refined.strip('"\'')
        print(f"[Mentor Prompt]: {refined}")
        return refined
    except Exception as e:
        print(f"[Mentor Error]: {e}")
        # 오류 시 기본 폴백
        return scene


@spaces.GPU
def generate_card(word: str, meaning: str, scene: str, style: str):
    """텍스트가 없는 순백 배경 원화를 만듭니다. 단어 표기는 웹에서 정확히 얹습니다."""
    word = (word or "").strip()
    meaning = (meaning or "").strip()
    scene = (scene or "").strip()
    
    # 영단어나 한글 뜻 중 하나만 입력해도 정상 동작하도록 가드 완화
    if not word and not meaning:
        raise gr.Error("영어 단어 또는 한글 뜻 중 최소 하나는 입력해야 합니다.")

    # 멘토링 함수를 통해 영어 프롬프트로 고도화
    refined_scene = mentor_scene(word, meaning, scene)

    style_guide = STYLE_GUIDES.get(style, STYLE_GUIDES["세밀 수채화"])
    
    # 아동용/동화용 친화 스타일일 때는 'no childish cartoon style' 가드 완화
    child_friendly = style in ["귀여운 3D 점토", "따뜻한 그림책"]
    cartoon_guard = "" if child_friendly else ", no childish cartoon style"

    prompt = f"""
    Create this exact scene: {refined_scene}.
    The main learning subject is the subject '{word if word else meaning}'
    ({meaning or 'vocabulary learning card'}). Use {style_guide}.
    Sophisticated educational editorial illustration for teenagers, centered and fully visible,
    balanced negative space, pure bright white background, crisp silhouette, elegant restrained colors,
    no text, no letters, no watermark, no frame, no hand{cartoon_guard}.
    """

    # 403 API 권한 제약을 우회하기 위해 공식 무료 FLUX 데모 스페이스로 직접 추론 호출 시도
    try:
        print("[Router] Trying direct inference through official FLUX Space...")
        temp_client = Client("black-forest-labs/FLUX.1-schnell")
        result = temp_client.predict(
            prompt=prompt,
            seed=0,
            width=1024,
            height=1024,
            num_inference_steps=4,
            api_name="/predict"
        )
        # 성공 시 로컬 임시 이미지 경로 반환
        return result
    except Exception as e:
        print(f"[Router Fallback] Direct inference failed: {e}. Falling back to InferenceClient...")
        return client.text_to_image(prompt, model=MODEL_ID)


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
