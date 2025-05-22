import streamlit as st
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import io
import os
from konlpy.tag import Okt
import urllib.request

# ✅ 폰트 자동 다운로드
font_path = "NanumGothic.ttf"
if not os.path.exists(font_path):
    st.info("🔤 'NanumGothic.ttf' 폰트가 없어서 자동 다운로드 중입니다...")
    url = "https://github.com/naver/nanumfont/blob/master/ttf/NanumGothic.ttf?raw=true"
    urllib.request.urlretrieve(url, font_path)
    st.success("✅ 폰트 다운로드 완료!")

st.set_page_config(page_title="한글 워드클라우드 생성기", layout="centered")
st.title("☁️ 한글 워드클라우드 생성기 (마스크 + 형태소 분석)")

st.markdown(\"\"\"
이 대시보드는 한글 텍스트를 업로드하고, 선택한 마스크 이미지에 맞춰 워드클라우드를 생성합니다.  
- `.txt` 파일로 텍스트를 업로드하세요  
- `.png` 또는 `.jpg` 마스크 이미지를 업로드하면 해당 모양으로 클라우드가 생성됩니다  
\"\"\")

uploaded_text = st.file_uploader("📂 텍스트 파일 (.txt)을 업로드하세요", type="txt")
uploaded_mask = st.file_uploader("🖼 마스크 이미지 업로드 (선택 사항, PNG/JPG)", type=["png", "jpg", "jpeg"])

if uploaded_text is not None:
    text = uploaded_text.read().decode("utf-8")

    # ✅ 형태소 분석 (명사만 추출)
    okt = Okt()
    nouns = okt.nouns(text)
    nouns = [n for n in nouns if len(n) > 1]
    text_nouns = " ".join(nouns)

    # ✅ 마스크 이미지 처리
    mask_array = None
    if uploaded_mask is not None:
        image = Image.open(uploaded_mask).convert("RGB")
        image = image.resize((800, 800))
        mask_array = np.array(image)

    # ✅ 불용어 설정
    stopwords = set(STOPWORDS)
    stopwords.update(["그리고", "하지만", "있다", "하는", "것", "수", "위한"])

    # ✅ 워드클라우드 생성
    wc = WordCloud(
        font_path=font_path,
        background_color="white",
        width=800,
        height=800,
        stopwords=stopwords,
        mask=mask_array
    ).generate(text_nouns)

    st.subheader("🎨 생성된 워드클라우드")
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.imshow(wc, interpolation='bilinear')
    ax.axis("off")
    st.pyplot(fig)
else:
    st.info("📄 텍스트 파일을 업로드하면 여기에 워드클라우드가 생성됩니다!")
