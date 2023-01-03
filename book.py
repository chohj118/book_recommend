
import pandas as pd
import numpy as np
import streamlit as st
from sklearn.metrics.pairwise import cosine_similarity
from IPython.display import display

# 페이지 제목 설정
st.set_page_config(
    page_icon='📚',
    page_title='이book 어때?',
    layout='wide'
)

# 헤더와 서브헤더 설정
st.header('📖도서추천시스템')
st.subheader('추천')

df = pd.read_csv('data/in_price.csv')
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
    df_sim = df.loc[sim.index, ["상품명", "설명",'관리분류', 'topic_words','IMAGE','판매가']].join(sim)
    return df_sim
  
st.sidebar.header('토픽을 선택해주세요')
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
page = st.radio('장르를 선택해주세요', page_name,  horizontal=True)

if page == page_name[0]:
    book1 = st.selectbox(f'{page_name[0]}을 선택해주세요', category[0])
    recommand = recommand(book1)
elif page == page_name[1]:
    book1 = st.selectbox(f'{page_name[1]}을 선택해주세요', category[1])
    recommand = recommand(book1)
elif page == page_name[2]:
    book1 = st.selectbox(f'{page_name[2]}을 선택해주세요', category[2])
    recommand = recommand(book1)
elif page == page_name[3]:
    book1 = st.selectbox(f'{page_name[3]}을 선택해주세요', category[3])
    recommand = recommand(book1)
else:
    if len(category_etc) == 0:
        st.write('책이 없습니다.')
    else:
        book1 = st.selectbox('선택해주세요', category_etc)
    recommand = recommand(book1)

container = st.container()
container.subheader(f"책 제목 : {recommand.iloc[0]['상품명']}")
container.write(f"카테고리 : {recommand.iloc[0]['관리분류']}")
container.write(f"설명 : {recommand.iloc[0]['설명']}")


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