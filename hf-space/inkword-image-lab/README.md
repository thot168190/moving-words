---
title: InkWord Image Lab
emoji: 🎨
colorFrom: green
colorTo: blue
sdk: gradio
sdk_version: 5.49.1
app_file: app.py
pinned: false
license: apache-2.0
---

# 보는 단어장 전용 이미지 연구실

1. 이 폴더의 파일로 대표님 계정에 새 Hugging Face Space를 만듭니다.
2. Space 설정의 Secrets에 `HF_TOKEN`을 등록합니다.
3. 사이트의 `public/learning/image-lab-config.js`에 Space 아이디를 입력합니다.

이 연구실은 단어뿐 아니라 사용자가 적은 **장면 설명**을 그대로 생성 요청에 사용합니다.
기존 챕터 이미지를 재사용하지 않습니다.

소스와 모델 공개 여부와 GPU 사용료는 별개입니다. Hugging Face 무료 크레딧 안에서는 무료로 시험할 수 있지만, 사용량이 커지면 Inference Provider 비용이 발생할 수 있습니다. 초기에는 월 10장 제한으로 운영합니다.
