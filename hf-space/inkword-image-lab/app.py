import os

import gradio as gr
from huggingface_hub import InferenceClient


MODEL_ID = os.getenv("MODEL_ID", "black-forest-labs/FLUX.1-schnell")
client = InferenceClient(token=os.getenv("HF_TOKEN"))

STYLE_GUIDES = {
    "세밀 수채화": "delicate museum-quality watercolor, refined fine-line details",
    "잉크 드로잉": "sophisticated fine ink drawing with restrained watercolor accents",
    "빈티지 도감": "elegant vintage natural-history plate, archival illustration",
    "밝은 파스텔": "refined luminous pastel illustration, soft yet not childish",
}


def generate_card(word: str, meaning: str, scene: str, style: str):
    """텍스트가 없는 순백 배경 원화를 만듭니다. 단어 표기는 웹에서 정확히 얹습니다."""
    word = (word or "").strip()
    meaning = (meaning or "").strip()
    scene = (scene or "").strip()
    if not word:
        raise gr.Error("영어 단어를 입력해주세요.")

    style_guide = STYLE_GUIDES.get(style, STYLE_GUIDES["세밀 수채화"])
    prompt = f"""
    Create this exact scene: {scene or f'a clear visual interpretation of {word}'}.
    The main learning subject is the English vocabulary word '{word}'
    ({meaning or 'vocabulary learning card'}). Use {style_guide}.
    Sophisticated educational editorial illustration for teenagers, centered and fully visible,
    balanced negative space, pure bright white background, crisp silhouette, elegant restrained colors,
    no text, no letters, no watermark, no frame, no hand, no childish cartoon style.
    """
    return client.text_to_image(prompt, model=MODEL_ID)


with gr.Blocks(title="InkWord Image Lab") as demo:
    gr.Markdown("# 보는 단어장 · 내가 만드는 그림 단어")
    with gr.Row():
        word_input = gr.Textbox(label="영어 단어", placeholder="예: telescope")
        meaning_input = gr.Textbox(label="한국어 뜻", placeholder="예: 망원경")
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
