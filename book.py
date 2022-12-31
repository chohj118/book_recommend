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
from sklearn.metrics.pairwise import cosine_similarity

# 페이지 제목 설정
st.set_page_config(
    page_icon='📚',
    page_title='이book 어때?',
    layout='wide'
)

# 헤더와 서브헤더 설정
st.header('도서추천시스템')
st.subheader('추천')

# 데이터 불러오기
df = pd.read_csv('data/topic_recommand_2.csv')
# df.set_index(keys=['상품명'], inplace=True)
# 코사인 유사도 매트릭스
df['topic_dict'] = df['topic_dict'].apply(lambda x: eval(x))
df_topic = pd.DataFrame(df['topic_dict'].tolist(), index=df.index).fillna(0)
cosine_matrix = cosine_similarity(df_topic, df_topic)

# 토픽 선택하기
def select_topic(topic):
    topic_index = df[df['top_topic']==(topic)].index
    return topic_index.tolist()

# 도서 추천시스템
def recommand(book):
    df_cosine = pd.DataFrame(cosine_matrix, index=df.index, columns=df.index)
    sim = df_cosine[book].sort_values(ascending=False)
    df_sim = df.loc[sim.index, ['상품명','관리분류', 'topic_words']].join(sim)
    return df_sim.head(10)

# topic = st.radio('topic을 선택해주세요', (df_topic.columns), horizontal=True)
# book = st.radio('책을 선택해주세요', (df.loc[select_topic(topic)].index), horizontal=True)
# st.dataframe(recommand(book))

topic = st.selectbox('토픽을 선택해주세요', options=(df_topic.columns.tolist()))
book = st.selectbox('책을 선택해주세요', options=(df.loc[select_topic(topic)].index.tolist()))
st.table(recommand(book))



# countplot 시각화
# fig, ax = plt.subplots(figsize=(20,10))
# sns.countplot(df[df['관리분류']=='에세이'], x='top_topic').set_title('에세이 분야 토픽 분포');
# st.pyplot(fig)

# fig, ax = plt.subplots(figsize=(20,10))
# ax.hist(df['관리분류'], bins=20)
# st.pyplot()