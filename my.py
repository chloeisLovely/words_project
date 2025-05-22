import streamlit as st

st.title("나의 첫 스트림릿 앱")
st.write("안녕하세요, 저는 데이터를 다루고 인공지능을 개발하는 **Chloe Lee** 입니다.")

st.title("이건 가장 큰 제목입니다!")
st.header("이건 두 번째로 큰 제목입니다!")
st.subheader("이건 세 번째 크기의 제목입니다!")
st.write("이건 일반 텍스트입니다.")

st.markdown("# 제일 큰 제목")
st.markdown("## 큰 제목")
st.markdown("### 보통 제목")
st.markdown("#### 작은 제목")
st.markdown("##### 더 작은 제목")
st.markdown("###### 제일 작은 제목")

st.markdown("**굵은 글씨**")
st.markdown("*기울어진 글씨*")
st.markdown("<span style='color:red'>빨간 글씨</span>", unsafe_allow_html=True) # unsafe_allow_html=True를 꼭 써야 색을 바꿀 수 있어
