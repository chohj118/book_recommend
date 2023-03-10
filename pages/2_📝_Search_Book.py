import pandas as pd
import numpy as np
import streamlit as st
import re

st.set_page_config(
    page_icon='π',
    page_title='μ΄Book μ΄λ?',
    layout='wide'
)

st.header('πμ΄Book μ΄λ?')
st.subheader('μ νν μ±κ³Ό μ μ¬ν λμ μΆμ²')
st.caption('λ¨μ΄λ‘ μλ ₯νμλ λ©λλ€')

df = pd.read_csv('data/final_file.csv')
df['topic_dict'] = df['topic_dict'].apply(lambda x: eval(x))
df_topic = pd.DataFrame(df['topic_dict'].tolist(), index=df.index).fillna(0)
pearson_sim = np.corrcoef(df_topic.to_numpy())

def select_topic(topic):
    topic_index = df[df['top_topic']==(topic)].index
    return topic_index.tolist()
def search_book(title):
    title = re.sub(r"\s", "", title)
    title_1 = df['μνλͺ'].apply(lambda x: re.sub(r"\s", "", x))
    book_title = df.loc[title_1.str.contains(title), "μνλͺ"].sort_values(ascending=True).tolist()
    return book_title
def choice_book(search):
    book_title = df.loc[df['μνλͺ'] == search, ['μνλͺ', 'μ±μκ°', 'κ΄λ¦¬λΆλ₯','IMAGE','νλ§€κ°','μ μ']]
    return book_title
def recommand(book):
    book_index = df[df['μνλͺ'] == book].index[0]
    df_pearson = pd.DataFrame(pearson_sim, index=df.index, columns=df.index)
    sim = df_pearson[book_index].sort_values(ascending=False)
    df_sim = df.loc[sim.index, ["μνλͺ", "μ±μκ°",'κ΄λ¦¬λΆλ₯', 'topic_words','IMAGE','νλ§€κ°','μ μ']].join(sim)
    return df_sim.head(11)

title = st.text_input('μνμλ μ±μ μ λͺ©μ μλ ₯νμΈμ.')

placeholder = st.empty()

if not title:
    placeholder.success("μλ ₯μ κΈ°λ€λ¦¬κ³  μμ΄μ.")
    

search = st.selectbox('μ΄ μ±μ΄ λ§λμ?', search_book(title))


if not search:
    placeholder.error("μ±μ μ°Ύμ μ μμ΅λλ€. μ λͺ©μ λ€μ νμΈν΄μ£ΌμΈμ.")
    
choice = choice_book(search)

col1, col2 = st.columns([0.3,0.6])
with col1:
    st.subheader(f"λΉμ μ΄ μ νν γ{choice['μνλͺ'].tolist()[0]}γμ κ΄ν λ΄μ©")
    st.image(choice['IMAGE'].tolist()[0],width=300)
with col2:
    st.markdown("##")
    st.markdown("##")
    st.markdown("##")
    st.markdown("##")
    st.markdown("##")
    st.markdown("##")
    st.write(f"πΈνλ§€κ°: {choice['νλ§€κ°'].tolist()[0]}")
    st.write(f"πμ μ: {choice['μ μ'].tolist()[0]}")
    st.write(f"πμΉ΄νκ³ λ¦¬ : {choice['κ΄λ¦¬λΆλ₯'].tolist()[0]}")
    st.write(f"πμ±μκ° : {choice['μ±μκ°'].tolist()[0]}")

recommand = recommand(search)

tabs_font_css = """
<style>
button[data-baseweb="tab"] {
  font-size: 13px;
}
</style>
"""

st.write(tabs_font_css, unsafe_allow_html=True)

st.header(f"γ{recommand.iloc[0]['μνλͺ']}γμ ν¨κ» μ΄ν΄λ³Ό λ§ν μ± 10κΆ")
st.caption('shift + scroll ππ')
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs([f"{recommand.iloc[i]['μνλͺ']}" for i in range(1,11)])
with tab1:
    col1, col2 = st.columns([0.3,0.6])
    with col1:
        st.header(f"{recommand.iloc[1]['μνλͺ']}")
        st.image(f"{recommand.iloc[1]['IMAGE']}",width=300)
    with col2:
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.write(f"πΈνλ§€κ°: {recommand.iloc[1]['νλ§€κ°']}")
        st.write(f"πμ μ: {recommand.iloc[1]['μ μ']}")
        st.write(f"πμΉ΄νκ³ λ¦¬ : {recommand.iloc[1]['κ΄λ¦¬λΆλ₯']}")
        st.write(f"πμ±μκ° : {recommand.iloc[1]['μ±μκ°']}")
with tab2:
    col1, col2 = st.columns([0.3,0.6])
    with col1:
        st.header(f"{recommand.iloc[2]['μνλͺ']}")
        st.image(f"{recommand.iloc[2]['IMAGE']}",width=300)
    with col2:
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.write(f"πΈνλ§€κ°: {recommand.iloc[2]['νλ§€κ°']}")
        st.write(f"πμ μ: {recommand.iloc[2]['μ μ']}")
        st.write(f"πμΉ΄νκ³ λ¦¬ : {recommand.iloc[2]['κ΄λ¦¬λΆλ₯']}")
        st.write(f"πμ±μκ° : {recommand.iloc[2]['μ±μκ°']}")
with tab3:
    col1, col2 = st.columns([0.3,0.6])
    with col1:
        st.header(f"{recommand.iloc[3]['μνλͺ']}")
        st.image(f"{recommand.iloc[3]['IMAGE']}",width=300)
    with col2:
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.write(f"πΈνλ§€κ°: {recommand.iloc[3]['νλ§€κ°']}")
        st.write(f"πμ μ: {recommand.iloc[3]['μ μ']}")
        st.write(f"πμΉ΄νκ³ λ¦¬ : {recommand.iloc[3]['κ΄λ¦¬λΆλ₯']}")
        st.write(f"πμ±μκ° : {recommand.iloc[3]['μ±μκ°']}")
with tab4:
    col1, col2 = st.columns([0.3,0.6])
    with col1:
        st.header(f"{recommand.iloc[4]['μνλͺ']}")
        st.image(f"{recommand.iloc[4]['IMAGE']}",width=300)
    with col2:
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.write(f"πΈνλ§€κ°: {recommand.iloc[4]['νλ§€κ°']}")
        st.write(f"πμ μ: {recommand.iloc[4]['μ μ']}")
        st.write(f"πμΉ΄νκ³ λ¦¬ : {recommand.iloc[4]['κ΄λ¦¬λΆλ₯']}")
        st.write(f"πμ±μκ° : {recommand.iloc[4]['μ±μκ°']}")
with tab5:
    col1, col2 = st.columns([0.3,0.6])
    with col1:
        st.header(f"{recommand.iloc[5]['μνλͺ']}")
        st.image(f"{recommand.iloc[5]['IMAGE']}",width=300)
    with col2:
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.write(f"πΈνλ§€κ°: {recommand.iloc[5]['νλ§€κ°']}")
        st.write(f"πμ μ: {recommand.iloc[5]['μ μ']}")
        st.write(f"πμΉ΄νκ³ λ¦¬ : {recommand.iloc[5]['κ΄λ¦¬λΆλ₯']}")
        st.write(f"πμ±μκ° : {recommand.iloc[5]['μ±μκ°']}")
with tab6:
    col1, col2 = st.columns([0.3,0.6])
    with col1:
        st.header(f"{recommand.iloc[6]['μνλͺ']}")
        st.image(f"{recommand.iloc[6]['IMAGE']}",width=300)
    with col2:
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.write(f"πΈνλ§€κ°: {recommand.iloc[6]['νλ§€κ°']}")
        st.write(f"πμ μ: {recommand.iloc[6]['μ μ']}")
        st.write(f"πμΉ΄νκ³ λ¦¬ : {recommand.iloc[6]['κ΄λ¦¬λΆλ₯']}")
        st.write(f"πμ±μκ° : {recommand.iloc[6]['μ±μκ°']}")
with tab7:
    col1, col2 = st.columns([0.3,0.6])
    with col1:
        st.header(f"{recommand.iloc[7]['μνλͺ']}")
        st.image(f"{recommand.iloc[7]['IMAGE']}",width=300)
    with col2:
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.write(f"πΈνλ§€κ°: {recommand.iloc[7]['νλ§€κ°']}")
        st.write(f"πμ μ: {recommand.iloc[7]['μ μ']}")
        st.write(f"πμΉ΄νκ³ λ¦¬ : {recommand.iloc[7]['κ΄λ¦¬λΆλ₯']}")
        st.write(f"πμ±μκ° : {recommand.iloc[7]['μ±μκ°']}")
with tab8:
    col1, col2 = st.columns([0.3,0.6])
    with col1:
        st.header(f"{recommand.iloc[8]['μνλͺ']}")
        st.image(f"{recommand.iloc[8]['IMAGE']}",width=300)
    with col2:
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.write(f"πΈνλ§€κ°: {recommand.iloc[8]['νλ§€κ°']}")
        st.write(f"πμ μ: {recommand.iloc[8]['μ μ']}")
        st.write(f"πμΉ΄νκ³ λ¦¬ : {recommand.iloc[8]['κ΄λ¦¬λΆλ₯']}")
        st.write(f"πμ±μκ° : {recommand.iloc[8]['μ±μκ°']}")
with tab9:
    col1, col2 = st.columns([0.3,0.6])
    with col1:
        st.header(f"{recommand.iloc[9]['μνλͺ']}")
        st.image(f"{recommand.iloc[9]['IMAGE']}",width=300)
    with col2:
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.write(f"πΈνλ§€κ°: {recommand.iloc[9]['νλ§€κ°']}")
        st.write(f"πμ μ: {recommand.iloc[9]['μ μ']}")
        st.write(f"πμΉ΄νκ³ λ¦¬ : {recommand.iloc[9]['κ΄λ¦¬λΆλ₯']}")
        st.write(f"πμ±μκ° : {recommand.iloc[9]['μ±μκ°']}")
with tab10:
    col1, col2 = st.columns([0.3,0.6])
    with col1:
        st.header(f"{recommand.iloc[10]['μνλͺ']}")
        st.image(f"{recommand.iloc[10]['IMAGE']}",width=300)
    with col2:
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.write(f"πΈνλ§€κ°: {recommand.iloc[10]['νλ§€κ°']}")
        st.write(f"πμ μ: {recommand.iloc[10]['μ μ']}")
        st.write(f"πμΉ΄νκ³ λ¦¬ : {recommand.iloc[10]['κ΄λ¦¬λΆλ₯']}")
        st.write(f"πμ±μκ° : {recommand.iloc[10]['μ±μκ°']}")
    
    
st.markdown("#")
st.write('π’μλ ννμ΄μ§μμ μνλ μ± μ λͺ©μ λ³΅μ¬ν΄ κ²μνμΈμ!')
st.write('yes24 ννμ΄μ§ : http://www.yes24.com/main/default.aspx')
st.markdown("#")
st.subheader("λ μ’μ μ±λ₯μ λ§λ€κΈ° μν΄ μ€λ¬Έ λΆνλλ €μ")
st.subheader(':https://docs.google.com/forms/d/e/1FAIpQLSd9mFcWH9Q1jCwV7CehiHpmzxU57a01dZiHojw5k5ffrfokHg/viewform')
