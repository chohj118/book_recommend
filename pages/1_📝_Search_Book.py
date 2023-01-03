import pandas as pd
import numpy as np
import streamlit as st

st.set_page_config(
    page_icon='📚',
    page_title='이book 어때?',
    layout='wide'
)

st.title('책 제목을 입력하세요')

df = pd.read_csv('data/in_price.csv')
df['topic_dict'] = df['topic_dict'].apply(lambda x: eval(x))
df_topic = pd.DataFrame(df['topic_dict'].tolist(), index=df.index).fillna(0)
pearson_sim = np.corrcoef(df_topic.to_numpy())

def select_topic(topic):
    topic_index = df[df['top_topic']==(topic)].index
    return topic_index.tolist()
def search_book(title):
    book_title = df.loc[df['상품명'].str.contains(title), "상품명"].sort_values().tolist()
    return book_title
def choice_book(search):
    book_title = df.loc[df['상품명'] == search, ['상품명', '설명', '관리분류']]
    return book_title
def recommand(book):
    book_index = df[df['상품명'] == book].index[0]
    df_pearson = pd.DataFrame(pearson_sim, index=df.index, columns=df.index)
    sim = df_pearson[book_index].sort_values(ascending=False)
    df_sim = df.loc[sim.index, ["상품명", "설명",'관리분류', 'topic_words','IMAGE','판매가']].join(sim)
    return df_sim.head(11)

title = st.text_input('원하시는 책의 제목을 입력하세요.')

search = st.selectbox('이 책이 맞으신가요?', search_book(title))
choice = choice_book(search)

container = st.container()
container.subheader(f"책제목 : {choice['상품명'].tolist()[0]}")
container.write(f"카테고리 : {choice['관리분류'].tolist()[0]}")
container.write(f"설명 : {choice['설명'].tolist()[0]}")

recommand = recommand(search)

st.header('📚책 추천 목록')
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10= st.tabs(['1번','2번','3번','4번','5번','6번','7번','8번','9번','10번'])
with tab1:
    st.header(f"{recommand.iloc[1]['상품명']}")
    st.image(f"{recommand.iloc[1]['IMAGE']}",width=300)
    st.write(f"판매가: {recommand.iloc[1]['판매가']}")
    st.write(f"카테고리 : {recommand.iloc[1]['관리분류']}")
    st.write(f"설명 : {recommand.iloc[1]['설명']}")
with tab2:
    st.header(f"{recommand.iloc[2]['상품명']}")
    st.image(f"{recommand.iloc[2]['IMAGE']}",width=300)
    st.write(f"판매가: {recommand.iloc[2]['판매가']}")
    st.write(f"카테고리 : {recommand.iloc[2]['관리분류']}")
    st.write(f"설명 : {recommand.iloc[2]['설명']}")
with tab3:
    st.header(f"{recommand.iloc[3]['상품명']}")
    st.image(f"{recommand.iloc[3]['IMAGE']}",width=300)
    st.write(f"판매가: {recommand.iloc[3]['판매가']}")
    st.write(f"카테고리 : {recommand.iloc[3]['관리분류']}")
    st.write(f"설명 : {recommand.iloc[3]['설명']}")
with tab4:
    st.header(f"{recommand.iloc[4]['상품명']}")
    st.image(f"{recommand.iloc[4]['IMAGE']}",width=300)
    st.write(f"판매가: {recommand.iloc[4]['판매가']}")
    st.write(f"카테고리 : {recommand.iloc[4]['관리분류']}")
    st.write(f"설명 : {recommand.iloc[4]['설명']}")
with tab5:
    st.header(f"{recommand.iloc[5]['상품명']}")
    st.image(f"{recommand.iloc[5]['IMAGE']}",width=300)
    st.write(f"판매가: {recommand.iloc[5]['판매가']}")
    st.write(f"카테고리 : {recommand.iloc[5]['관리분류']}")
    st.write(f"설명 : {recommand.iloc[5]['설명']}")
with tab6:
    st.header(f"{recommand.iloc[6]['상품명']}")
    st.image(f"{recommand.iloc[6]['IMAGE']}",width=300)
    st.write(f"판매가: {recommand.iloc[6]['판매가']}")
    st.write(f"카테고리 : {recommand.iloc[6]['관리분류']}")
    st.write(f"설명 : {recommand.iloc[6]['설명']}")
with tab7:
    st.header(f"{recommand.iloc[7]['상품명']}")
    st.image(f"{recommand.iloc[7]['IMAGE']}",width=300)
    st.write(f"판매가: {recommand.iloc[7]['판매가']}")
    st.write(f"카테고리 : {recommand.iloc[7]['관리분류']}")
    st.write(f"설명 : {recommand.iloc[7]['설명']}")
with tab8:
    st.header(f"{recommand.iloc[8]['상품명']}")
    st.image(f"{recommand.iloc[8]['IMAGE']}",width=300)
    st.write(f"판매가: {recommand.iloc[8]['판매가']}")
    st.write(f"카테고리 : {recommand.iloc[8]['관리분류']}")
    st.write(f"설명 : {recommand.iloc[8]['설명']}")
with tab9:
    st.header(f"{recommand.iloc[9]['상품명']}")
    st.image(f"{recommand.iloc[9]['IMAGE']}",width=300)
    st.write(f"판매가: {recommand.iloc[9]['판매가']}")
    st.write(f"카테고리 : {recommand.iloc[9]['관리분류']}")
    st.write(f"설명 : {recommand.iloc[9]['설명']}")
with tab10:
    st.header(f"{recommand.iloc[10]['상품명']}")
    st.image(f"{recommand.iloc[10]['IMAGE']}",width=300)
    st.write(f"판매가: {recommand.iloc[10]['판매가']}")
    st.write(f"카테고리 : {recommand.iloc[10]['관리분류']}")
    st.write(f"설명 : {recommand.iloc[10]['설명']}")
    
    
st.write('\-'*180)
st.write('아래 홈페이지에서 원하는 책 제목을 복사해 검색하세요!')
st.write('yes24 홈페이지 : http://www.yes24.com/main/default.aspx')