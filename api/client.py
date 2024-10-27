import requests
import streamlit as st

def get_gemma_response(input_text):
    response=requests.post(
        "http://localhost:8000/essay/invoke",
        json={'input':{'topic':input_text}}
    )

def get_llama_response(input_text):
    response=requests.post(
        "http://localhost:8000/poem/invoke",
        json={'input':{'topic':input_text}}
    )
    return response.json()['output']

st.title('LangChain Demo with LLAMA and Gemma API')
input_text_1=st.text_input("Topic for essay")
input_text_2=st.text_input("Topic for poem")

if input_text_1:
    st.write(get_gemma_response(input_text_1))

if input_text_1:
    st.write(get_llama_response(input_text_2))