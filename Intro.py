import streamlit as st

st.set_page_config(
    page_icon='📚',
    page_title='이book 어때?',
    layout='wide'
)

st.markdown('#')
st.markdown('### 🧐  매년마다 사람들의 독서량이 줄어들고 있는 이유는 뭘까❓')
st.markdown('### 🥱 넘쳐나는 컨텐츠들 중 자신이 원하는 책들을 바로 찾아내기 어렵기 때문❗')
st.markdown('### 👨🏻‍💻 유저의 🌟취.향.저.격🌟 책을 추천해주자 👩🏻‍💻')
st.markdown('#')
st.image('data/img0.jpg',width=900)

st.markdown('#')
st.markdown('## 📔 이렇게 사용해보세요')


col1, col2 = st.columns([0.3,0.6])
with col1:
    st.markdown('### 1️⃣ Keyword Recommend')
    st.markdown('1.사이드 바에 있는 토픽 중 마음에 드는 토픽을 선택👈하세요')
    st.markdown('2.장르를 선택하시면 해당 토픽에 해당하는 장르만 보여줍니다!')
    st.markdown('3.리스트를 열어보고 마음에 콕💘 박히는 책을 눌러보세요')
    st.markdown('4.스크롤을 내려보면 선택한 책과 유사한 책들이 보일거에요!😍 ')
with col2:
    st.markdown('### 2️⃣ Search Book')
    st.markdown('1.원하시는 책 제목을 입력🔎해주세요~!')
    st.markdown('💡꿀팁! 단어만 입력해도 책이 나온답니다💡')
    st.markdown('2.리스트를 열어봐서 해당 책을 누르면!! 유사한 책들이 나옵니다🍀')

st.markdown('#')
st.markdown('## 🎇이제 직접 해보세요!')