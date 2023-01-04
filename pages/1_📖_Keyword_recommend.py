import pandas as pd
import numpy as np
import streamlit as st

# 페이지 제목 설정
st.set_page_config(
    page_icon='📚',
    page_title='이Book 어때?',
    layout='wide'
)

# 헤더와 서브헤더 설정
st.header('📚이Book 어때?')
st.subheader('키워드 기반 도서 추천')

df = pd.read_csv('data/final_file.csv')
df['topic_dict'] = df['topic_dict'].apply(lambda x: eval(x))
df_topic = pd.DataFrame(df['topic_dict'].tolist(), index=df.index).fillna(0)
pearson_sim = np.corrcoef(df_topic.to_numpy())


def select_topic(topic):
    topic_index = df[df['topic_words']==(topic)].index
    return topic_index.sort_values(ascending=True).tolist()

def recommand(book):
    book_index = topic_df[topic_df['상품명'] == book].index[0]
    df_pearson = pd.DataFrame(pearson_sim, index=df.index, columns=df.index)
    sim = df_pearson[book_index].sort_values(ascending=False)
    df_sim = df.loc[sim.index, ["상품명", "책소개",'관리분류', 'topic_words','IMAGE','판매가','저자']].join(sim)
    return df_sim
  
st.sidebar.header('관심 키워드를 선택해주세요')
topic = st.sidebar.radio('', (df['topic_words'].value_counts().index))
topic_name = select_topic(topic)
category_index = df.loc[topic_name, '관리분류'].value_counts().index
topic_df = df.loc[topic_name]
category = []
category_etc=[]
page_name = []

for v, i in enumerate(category_index):
    if v <= 3:
        category.append(topic_df[topic_df['관리분류'] == i]['상품명'].sort_values().tolist())
        page_name.append(category_index[v])
    else:
        category_etc.extend(topic_df[topic_df['관리분류'] == i]['상품명'].sort_values().tolist())
        

page_name.append('그 외')
page = st.radio('선택한 관심 키워드를 장르별로 분류해서 보여드릴게요', page_name,  horizontal=True)

if page == page_name[0]:
    book1 = st.selectbox(f'{page_name[0]}장르의 책을 선택해주세요', category[0])
    recommand = recommand(book1)
elif page == page_name[1]:
    book1 = st.selectbox(f'{page_name[1]}장르의 책을 선택해주세요', category[1])
    recommand = recommand(book1)
elif page == page_name[2]:
    book1 = st.selectbox(f'{page_name[2]}장르의 책을 선택해주세요', category[2])
    recommand = recommand(book1)
elif page == page_name[3]:
    book1 = st.selectbox(f'{page_name[3]}장르의 책을 선택해주세요', category[3])
    recommand = recommand(book1)
else:
    if len(category_etc) == 0:
        st.write('🚫책이 없습니다.')
    else:
        book1 = st.selectbox('💡책을 선택해주세요', category_etc)
    recommand = recommand(book1)

st.markdown('## ')
col1, col2 = st.columns([0.3,0.6])
with col1:
    st.subheader(f"당신이 선택한 『{recommand.iloc[0]['상품명']}』에 관한 내용")
    st.image(f"{recommand.iloc[0]['IMAGE']}",width=300)
with col2:
    st.markdown("##")
    st.markdown("##")
    st.markdown("##")
    st.markdown("##")
    st.markdown("##")
    st.markdown("##")
    st.write(f"💸판매가: {recommand.iloc[0]['판매가']}")
    st.write(f"📝저자: {recommand.iloc[0]['저자']}")
    st.write(f"📁카테고리 : {recommand.iloc[0]['관리분류']}")
    st.write(f"🔎책소개 : {recommand.iloc[0]['책소개']}")

tabs_font_css = """
<style>
button[data-baseweb="tab"] {
  font-size: 13px;
}
</style>
"""

st.write(tabs_font_css, unsafe_allow_html=True)


st.header(f"『{recommand.iloc[0]['상품명']}』와 함께 살펴볼 만한 책 10권")
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
        st.write('')
        st.write(f"📝저자: {recommand.iloc[1]['저자']}")
        st.write(f"📁카테고리 : {recommand.iloc[1]['관리분류']}")
        st.write('')
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
        st.write('')
        st.write(f"📝저자: {recommand.iloc[2]['저자']}")
        st.write(f"📁카테고리 : {recommand.iloc[2]['관리분류']}")
        st.write('')
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
        st.write('')
        st.write(f"📝저자: {recommand.iloc[3]['저자']}")
        st.write(f"📁카테고리 : {recommand.iloc[3]['관리분류']}")
        st.write('')
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
        st.write('')
        st.write(f"📝저자: {recommand.iloc[4]['저자']}")
        st.write(f"📁카테고리 : {recommand.iloc[4]['관리분류']}")
        st.write('')
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
        st.write('')
        st.write(f"📝저자: {recommand.iloc[5]['저자']}")
        st.write(f"📁카테고리 : {recommand.iloc[5]['관리분류']}")
        st.write('')
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
        st.write('')
        st.write(f"📝저자: {recommand.iloc[6]['저자']}")
        st.write(f"📁카테고리 : {recommand.iloc[6]['관리분류']}")
        st.write('')
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
        st.markdown("#")
        st.write(f"💸판매가: {recommand.iloc[7]['판매가']}")
        st.write('')
        st.write(f"📝저자: {recommand.iloc[7]['저자']}")
        st.write(f"📁카테고리 : {recommand.iloc[7]['관리분류']}")
        st.write('')
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
        st.write('')
        st.write(f"📝저자: {recommand.iloc[8]['저자']}")
        st.write(f"📁카테고리 : {recommand.iloc[8]['관리분류']}")
        st.write('')
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
        st.write('')
        st.write(f"📝저자: {recommand.iloc[9]['저자']}")
        st.write(f"📁카테고리 : {recommand.iloc[9]['관리분류']}")
        st.write('')
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
        st.write('')
        st.write(f"📝저자: {recommand.iloc[10]['저자']}")
        st.write(f"📁카테고리 : {recommand.iloc[10]['관리분류']}")
        st.write('')
        st.write(f"🔎책소개 : {recommand.iloc[10]['책소개']}")
    

st.markdown("#")
st.write('📢아래 홈페이지에서 원하는 책 제목을 복사해 검색하세요!')
st.write('yes24 홈페이지 : http://www.yes24.com/main/default.aspx')
st.markdown("#")
st.subheader("더 좋은 성능을 위해 설문 부탁드려요!")
st.subheader(':https://docs.google.com/forms/d/e/1FAIpQLSd9mFcWH9Q1jCwV7CehiHpmzxU57a01dZiHojw5k5ffrfokHg/viewform')