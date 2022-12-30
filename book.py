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
df = pd.read_csv('data/token.csv')
st.dataframe(df)

df['설명'] = df['설명_okt']
df = df[['순위', 'mean', 'ISBN', '상품명', '저자', '출판사', '설명', '관리분류']]
# 설명 컬럼 정규표현식
df['설명'] = df["설명"].str.replace('[^가-힣ㄱ-ㅎㅏ-ㅣa-zA-Z ]', "", regex=True)

# 불용어
stopwords = ["합니다", "입니다", "있다", "이 책은", "이", '점', '기', 
        "그", "베스트셀러", "등", "것을", "저자가", "된다", 
        "있는", "위해", "책은", "그리고", "년", "대한", "통해", "저자는", "수 있도록", "것이다", "을", "것", "내", "의", "개의", "더", "될", "개", 
        "및", "여", "각", "때", "중", "때", "전", "은", "건", "어떻게", "를", "는", "내가", "만", '할', '후', 
        "후", "을", "에", "로", "대해", "모든", "한", "된", "다", "되었다", "개의", "더", "될", "개", 
        "및", "여", "각", "때", "중", "때", "전", "은", "건", "어떻게", "를", "는", "내가", "만", 
        "수", "것은", "위한", "아니라", "우리가", "있습니다", "어떤", '간', '부', '것', '무엇', 
        '것', '책', '동안', '첫', '안', '를', '등', '곳', '왜', '의', '이', '작', 
        '그', '간', '위', '우리', '나', '년', '온', '누구', '알', '때', '권', '돌아왔', "찾아왔", "밝아졌", 
        '이야기', '때문', '속', '태어났', '받아들였', "일어났", '풀어졌', '만났', "해", "설서", "올랐", 
        "베스트셀러" , "출간", "말", "분야", "최고", "말", "독자", "동안", "때", "일", "집", "날", '생각', '문제', 
        "순간", "이후", "시간", "기록", "이상", "최초", '무엇', '팩', '션', '간', '단', '번', '레', '기', '후', '그', '장' 
        '해', '주요', 'ㄱ', 'ㅂ', 'ㅅ', 'ㅎ', '권은', '은', '장', '몰', '튜브', '우리', '이야기', '자신', '망', '린', '호', '점'
        '유', '등', '년', '그', '파', '방', '작가', '이야기', '독자', '출간', '나', '자신', '뭐', '한국', '대한민국', '글', '스스', 
        "션", "에디", "부", "나", "하나", "살", "일", "권", "세", "두", "이제", "때", '잇습니다', '가', '틱낫', '편', '개정', '판', '특징',
        "번", "관", "이", "티니", "실록", "간", "스", "작", "회", "자기", "곳", '것이', '치', '지금', '당신', '못', '징', '니로', '과', '고'
        '단', '아이히만은', '국립어린이청소년도서관', '도서', '권장도서', '나' '시간' '글', '때', "이것", '독자', '다른', '질문', '에세이', '목', '깃', '서',
        '그림', '세상', '오늘', '하루', '문장', '선정', '번역', '대표', '월', '기', '저자', '모두', '다시', '또', '드잉', '북', '무', '일상', '법', '눈', '매일', '줄']

# 불용어 제거 함수
# @st.cache
def remove_stop(text):
        token = text.split(" ")
        stops = stopwords
        meaningful_words = [w for w in token if  w not in stops]
        return ' '.join(meaningful_words)
    
# 불용어 함수 적용
df["설명"] = df["설명"].map(lambda x : remove_stop(x))
df["설명"] = df['설명'].str.replace("[\s]+", " ", regex=True)
df['설명'] = df['설명'].str.replace("['글']", '', regex=True)
df['설명'] = df['설명'].str.replace("['관계']", '', regex=True)
df['설명'] = df['설명'].str.replace("['바로']", '', regex=True)
df['설명'] = df['설명'].str.replace("['위']", '', regex=True)
df['설명'] = df['설명'].str.replace("['유튜브']", '', regex=True)
df["설명"] = df['설명'].str.replace("[\s]+", " ", regex=True)

# 토픽모델링
# @st.cache
class TopicModeling :
    # 최소 5개 이상 설명에 등장하고
    # 전체 출현빈도는 15개 이상인 단어만 사용
    def __init__(self, df, k, min_df=10, min_cf=10) : 
        self.df = df
        self.k = k  # 토픽의 개수
        self.min_df = min_df
        self.min_cf = min_cf

    def LDA(self) :

        LDA_model = tp.LDAModel(k=self.k, min_df=self.min_df, min_cf=self.min_cf, tw=tp.TermWeight.ONE, rm_top=1,
                                alpha=0.1, eta=0.01)
        for token in self.df['설명'].str.split(' '):
            LDA_model.add_doc(token)

        return LDA_model

    def train(self, LDA_model):
        LDA_model.train(0)
        print("Num docs :", len(LDA_model.docs), ', vocab_size:', LDA_model.num_vocabs, ', Num words:', LDA_model.num_words)
        print('Removed top word: ', LDA_model.removed_top_words)
        print('Training...', file=sys.stderr, flush=True) 
        for i in range(0, 1000, 100):
            LDA_model.train(100)
            print("Iteration : {}\tLog-likelihood: {}".format(i, LDA_model.ll_per_word))

    def result(self, LDA_model):
        for i in range(LDA_model.k):
            res = LDA_model.get_topic_words(i, top_n=10)
            print("Topic #{}".format(i), end='\t')
            print(', '.join(w for w, p in res))
    
    def get_coherence(self, LDA_model):
        coherence = tp.coherence
        score = coherence.Coherence(LDA_model).get_score()
        perplexity = LDA_model.perplexity
        print("topic 개수 : ", self.k, "| 사용된 vocab 수 : ", len(LDA_model.used_vocabs) , "| Coherence 점수 : ", score, 
                "| Perplexity 점수 : ", perplexity)
        return score, perplexity
    
# 트레이닝
lda = TopicModeling(df, 20)
model = lda.LDA()
lda.train(model)
len(model.used_vocabs)
lda.result(model)
lda.get_coherence(model)

# 토픽 관련 항목 추가
# df['top_topic'] = 0
# df['topic_dist'] = 0
# df['topic_words'] = 0

# for i in tqdm(range(len(model.docs))):
#     df["topic_dist"][i] = model.docs[i].get_topics(top_n=4)
#     df['top_topic'][i] = model.docs[i].get_topics()[0][0]
#     res = model.get_topic_words(df['top_topic'][i], top_n=5)
#     df["topic_words"][i] = ' '.join(w for w, p in res)
    
st.dataframe(df[['상품명','top_topic','topic_words']])

# countplot 시각화
# fig, ax = plt.subplots(figsize=(20,10))
# sns.countplot(df[df['관리분류']=='에세이'], x='top_topic').set_title('에세이 분야 토픽 분포');
# st.pyplot(fig)

