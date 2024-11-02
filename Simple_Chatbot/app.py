from langchain_openai import ChatOpenAI # type: ignore
from langchain_core.prompts import ChatPromptTemplate # type: ignore
from langchain_core.output_parsers import StrOutputParser # type: ignore
from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

##LangSmith Tracking

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

##Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a gangster assistant. Please respond to user queries accordingly."),
        ("user","Question:{question}")
    ]
)

##Streamlit Framework

st.title('Chatbot')
input_text=st.text_input("Search for the Topic")

llm=Ollama(model="llama3.1")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))