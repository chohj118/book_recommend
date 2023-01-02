import streamlit as st
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import seaborn as sns
import tomotopy as tp
import sys
import logging
from tqdm import tqdm
import koreanize_matplotlib
from wordcloud import WordCloud
from sklearn.metrics.pairwise import cosine_similarity
from PIL import Image

# 페이지 제목 설정
st.set_page_config(
    page_icon='📚',
    page_title='이book 어때?',
    layout='wide'
)

# 헤더와 서브헤더 설정
st.header('도서추천시스템📕')
st.subheader('이런 책은 어떠세요?')

# 데이터 불러오기
df = pd.read_csv('data/topic_recommand_2.csv')
df.set_index(keys=['상품명'], inplace=True)


# 코사인 유사도 매트릭스
df['topic_dict'] = df['topic_dict'].apply(lambda x: eval(x))
df_topic = pd.DataFrame(df['topic_dict'].tolist(), index=df.index).fillna(0)
cosine_matrix = cosine_similarity(df_topic, df_topic)

# 토픽 선택하기
def select_topic(topic):
    topic_index = df[df['top_topic']==(topic)].index
    return topic_index.sort_values(ascending=True).tolist()

def recommand(book):
    df_cosine = pd.DataFrame(cosine_matrix, index=df.index, columns=df.index)
    df_sub = df[['mean','관리분류']]
    df_sim =pd.concat([df_cosine,df_sub],axis=1)
    return df_sim[[book,'mean','관리분류']].sort_values(by=book,ascending=False)

# 사이드바 적용
topic = st.sidebar.radio('토픽을 선택해주세요', options=(df_topic.columns), horizontal=True)
book = st.sidebar.selectbox('책을 선택해주세요', options=(select_topic(topic)))

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.dataframe(recommand(book)[1:11])
    
    
with col2:
    st.dataframe(recommand(book)[1:11])
    
with col3:
    st.dataframe(recommand(book)[1:11])

with col4:
    st.dataframe(recommand(book)[1:11])

# countplot 시각화
# fig, ax = plt.subplots(figsize=(20,10))
# sns.countplot(df[df['관리분류']=='에세이'], x='top_topic').set_title('에세이 분야 토픽 분포');
# st.pyplot(fig)

# fig, ax = plt.subplots(figsize=(20,10))
# ax.hist(df['관리분류'], bins=20)
# st.pyplot()


# radio 형태로 선택
# topic = st.radio('topic을 선택해주세요', (df_topic.columns), horizontal=True)
# book = st.radio('책을 선택해주세요', (df.loc[select_topic(topic)].index), horizontal=True)
# st.dataframe(recommand(book))

# selectbox 형태로 선택
# topic = st.selectbox('토픽을 선택해주세요', options=(df_topic.columns))
# book = st.selectbox('책을 선택해주세요', options=(select_topic(topic)))
# st.dataframe(recommand(book).head(10))

# 도서 추천시스템
# def recommand(book):
#     df_cosine = pd.DataFrame(cosine_matrix, index=df.index, columns=df.index)
#     sim = df_cosine[book].sort_values(ascending=False)
#     df_sim = df.loc[sim.index,['관리분류', 'topic_words']].join(sim).sort_values(sim)
#     return df_sim