import streamlit as st

st.set_page_config(
    page_icon='📚',
    page_title='이Book 어때?',
    layout='wide'
)

st.title('[이Book 어때?] 키워드 기반 도서 추천시스템')
st.markdown('## Introduction')
st.markdown('###   매년 사람들의 독서량은 줄어들고만 있습니다.')
st.markdown('###   컨텐츠의 홍수 속에서 원하는 책을 골라내는 게 어렵다고 느끼신 적 있나요?')
st.markdown('###   이Book 어때?가 당신의 💘 취.향.저.격. 책을 추천해드릴게요. ')
st.markdown('#')
st.image('data/img0.jpg',width=900)

st.markdown('#')
st.markdown('## Guide')


col1, col2 = st.columns([0.4,0.5])
with col1:
    st.markdown('### 1️⃣ Keyword Recommend')
    st.markdown('1. 사이드 바의 관심 키워드 중 하나를 선택하세요.')
    st.markdown('2. 원하는 장르를 선택합니다.')
    st.markdown('   선택하신 키워드를 가진 해당 장르의 책을 구경할 수 있습니다.')
    st.markdown('3. 목록 중 마음에 콕 박히는 책 하나를 선택하세요.')
    st.markdown('4. 스크롤을 내리면, 선택한 책과 유사한 책들이 더 보일 거예요!')
with col2:
    st.markdown('### 2️⃣ Search Book')
    st.markdown('1. 원하는 책 제목을 입력하세요.')
    st.markdown('💡 꿀팁! 단어를 통해 검색할 수도 있어요')
    st.markdown('2. 목록에서 책을 골라가며 10가지 책 추천을 받아보세요.')

st.markdown('#')
st.markdown('## 이제 직접 책을 추천받으러 가볼까요? 🧚')