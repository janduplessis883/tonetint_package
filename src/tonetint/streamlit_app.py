import streamlit as st

st.title("ToneTint")

selected_model = st.selectbox("Pick a Text Classification Model", options=["nlptown/bert-base-multilingual-uncased-sentiment", "cardiffnlp/twitter-roberta-base-sentiment-latest", "citizenlab/twitter-xlm-roberta-base-sentiment-finetunned",])
text_area = st.text_area("Paste Text here")
