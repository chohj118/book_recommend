import pandas as pd
import numpy as np
import streamlit as st
import re

st.set_page_config(
    page_icon='📚',
    page_title='이book 어때?',
    layout='wide'
)

st.header('📚이book 어때?')
st.subheader('📖선택한 책과 유사한 도서 추천')
st.caption('📢단어로 입력하셔도 됩니다')

df = pd.read_csv('data/final_file.csv')
df['topic_dict'] = df['topic_dict'].apply(lambda x: eval(x))
df_topic = pd.DataFrame(df['topic_dict'].tolist(), index=df.index).fillna(0)
pearson_sim = np.corrcoef(df_topic.to_numpy())

def select_topic(topic):
    topic_index = df[df['top_topic']==(topic)].index
    return topic_index.tolist()
def search_book(title):
    title = re.sub(r"\s", "", title)
    title_1 = df['상품명'].apply(lambda x: re.sub(r"\s", "", x))
    book_title = df.loc[title_1.str.contains(title), "상품명"].sort_values(ascending=True).tolist()
    return book_title
def choice_book(search):
    book_title = df.loc[df['상품명'] == search, ['상품명', '책소개', '관리분류','IMAGE','판매가','저자']]
    return book_title
def recommand(book):
    book_index = df[df['상품명'] == book].index[0]
    df_pearson = pd.DataFrame(pearson_sim, index=df.index, columns=df.index)
    sim = df_pearson[book_index].sort_values(ascending=False)
    df_sim = df.loc[sim.index, ["상품명", "책소개",'관리분류', 'topic_words','IMAGE','판매가','저자']].join(sim)
    return df_sim.head(11)

title = st.text_input('💡원하시는 책의 제목을 입력하세요.')

placeholder = st.empty()

if not title:
    placeholder.success("입력을 기다리고 있어요.")
    

search = st.selectbox('🧐이 책이 맞나요?', search_book(title))


if not search:
    placeholder.error("책을 찾을 수 없습니다. 제목을 다시 확인해주세요.")
    
choice = choice_book(search)

col1, col2 = st.columns([0.3,0.6])
with col1:
    st.subheader(f"{choice['상품명'].tolist()[0]}")
    st.image(choice['IMAGE'].tolist()[0],width=300)
with col2:
    st.markdown("##")
    st.markdown("##")
    st.markdown("##")
    st.markdown("##")
    st.markdown("##")
    st.markdown("##")
    st.write(f"💸판매가: {choice['판매가'].tolist()[0]}")
    st.write(f"📝저자: {choice['저자'].tolist()[0]}")
    st.write(f"📁카테고리 : {choice['관리분류'].tolist()[0]}")
    st.write(f"🔎책소개 : {choice['책소개'].tolist()[0]}")

recommand = recommand(search)

tabs_font_css = """
<style>
button[data-baseweb="tab"] {
  font-size: 13px;
}
</style>
"""

st.write(tabs_font_css, unsafe_allow_html=True)

st.header('📚책 추천 목록')
st.caption('shift + scroll 👉👉')
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs([f"{recommand.iloc[i]['상품명']}" for i in range(1,11)])
with tab1:
    col1, col2 = st.columns([0.3,0.6])
    with col1:
        st.header(f"{recommand.iloc[1]['상품명']}")
        st.image(f"{recommand.iloc[1]['IMAGE']}",width=300)
    with col2:
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.write(f"💸판매가: {recommand.iloc[1]['판매가']}")
        st.write(f"📝저자: {recommand.iloc[1]['저자']}")
        st.write(f"📁카테고리 : {recommand.iloc[1]['관리분류']}")
        st.write(f"🔎책소개 : {recommand.iloc[1]['책소개']}")
with tab2:
    col1, col2 = st.columns([0.3,0.6])
    with col1:
        st.header(f"{recommand.iloc[2]['상품명']}")
        st.image(f"{recommand.iloc[2]['IMAGE']}",width=300)
    with col2:
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.write(f"💸판매가: {recommand.iloc[2]['판매가']}")
        st.write(f"📝저자: {recommand.iloc[2]['저자']}")
        st.write(f"📁카테고리 : {recommand.iloc[2]['관리분류']}")
        st.write(f"🔎책소개 : {recommand.iloc[2]['책소개']}")
with tab3:
    col1, col2 = st.columns([0.3,0.6])
    with col1:
        st.header(f"{recommand.iloc[3]['상품명']}")
        st.image(f"{recommand.iloc[3]['IMAGE']}",width=300)
    with col2:
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.write(f"💸판매가: {recommand.iloc[3]['판매가']}")
        st.write(f"📝저자: {recommand.iloc[3]['저자']}")
        st.write(f"📁카테고리 : {recommand.iloc[3]['관리분류']}")
        st.write(f"🔎책소개 : {recommand.iloc[3]['책소개']}")
with tab4:
    col1, col2 = st.columns([0.3,0.6])
    with col1:
        st.header(f"{recommand.iloc[4]['상품명']}")
        st.image(f"{recommand.iloc[4]['IMAGE']}",width=300)
    with col2:
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.write(f"💸판매가: {recommand.iloc[4]['판매가']}")
        st.write(f"📝저자: {recommand.iloc[4]['저자']}")
        st.write(f"📁카테고리 : {recommand.iloc[4]['관리분류']}")
        st.write(f"🔎책소개 : {recommand.iloc[4]['책소개']}")
with tab5:
    col1, col2 = st.columns([0.3,0.6])
    with col1:
        st.header(f"{recommand.iloc[5]['상품명']}")
        st.image(f"{recommand.iloc[5]['IMAGE']}",width=300)
    with col2:
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.write(f"💸판매가: {recommand.iloc[5]['판매가']}")
        st.write(f"📝저자: {recommand.iloc[5]['저자']}")
        st.write(f"📁카테고리 : {recommand.iloc[5]['관리분류']}")
        st.write(f"🔎책소개 : {recommand.iloc[5]['책소개']}")
with tab6:
    col1, col2 = st.columns([0.3,0.6])
    with col1:
        st.header(f"{recommand.iloc[6]['상품명']}")
        st.image(f"{recommand.iloc[6]['IMAGE']}",width=300)
    with col2:
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.write(f"💸판매가: {recommand.iloc[6]['판매가']}")
        st.write(f"📝저자: {recommand.iloc[6]['저자']}")
        st.write(f"📁카테고리 : {recommand.iloc[6]['관리분류']}")
        st.write(f"🔎책소개 : {recommand.iloc[6]['책소개']}")
with tab7:
    col1, col2 = st.columns([0.3,0.6])
    with col1:
        st.header(f"{recommand.iloc[7]['상품명']}")
        st.image(f"{recommand.iloc[7]['IMAGE']}",width=300)
    with col2:
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.write(f"💸판매가: {recommand.iloc[7]['판매가']}")
        st.write(f"📝저자: {recommand.iloc[7]['저자']}")
        st.write(f"📁카테고리 : {recommand.iloc[7]['관리분류']}")
        st.write(f"🔎책소개 : {recommand.iloc[7]['책소개']}")
with tab8:
    col1, col2 = st.columns([0.3,0.6])
    with col1:
        st.header(f"{recommand.iloc[8]['상품명']}")
        st.image(f"{recommand.iloc[8]['IMAGE']}",width=300)
    with col2:
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.write(f"💸판매가: {recommand.iloc[8]['판매가']}")
        st.write(f"📝저자: {recommand.iloc[8]['저자']}")
        st.write(f"📁카테고리 : {recommand.iloc[8]['관리분류']}")
        st.write(f"🔎책소개 : {recommand.iloc[8]['책소개']}")
with tab9:
    col1, col2 = st.columns([0.3,0.6])
    with col1:
        st.header(f"{recommand.iloc[9]['상품명']}")
        st.image(f"{recommand.iloc[9]['IMAGE']}",width=300)
    with col2:
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.write(f"💸판매가: {recommand.iloc[9]['판매가']}")
        st.write(f"📝저자: {recommand.iloc[9]['저자']}")
        st.write(f"📁카테고리 : {recommand.iloc[9]['관리분류']}")
        st.write(f"🔎책소개 : {recommand.iloc[9]['책소개']}")
with tab10:
    col1, col2 = st.columns([0.3,0.6])
    with col1:
        st.header(f"{recommand.iloc[10]['상품명']}")
        st.image(f"{recommand.iloc[10]['IMAGE']}",width=300)
    with col2:
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.write(f"💸판매가: {recommand.iloc[10]['판매가']}")
        st.write(f"📝저자: {recommand.iloc[10]['저자']}")
        st.write(f"📁카테고리 : {recommand.iloc[10]['관리분류']}")
        st.write(f"🔎책소개 : {recommand.iloc[10]['책소개']}")
    
    
st.markdown("#")
st.write('📢아래 홈페이지에서 원하는 책 제목을 복사해 검색하세요!')
st.write('🌐yes24 홈페이지 : http://www.yes24.com/main/default.aspx')
