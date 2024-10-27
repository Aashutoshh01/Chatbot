from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()

app=FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple API server"
)

llm_gemma=Ollama(model="gemma2:2b")
llm_llama=Ollama(model="llama3.1")

prompt1=ChatPromptTemplate.from_template("Write an essay about {topic} with 100 words in shakespeare language.")
prompt2=ChatPromptTemplate.from_template("Write a poem about {topic} in shakespeare language.")

add_routes(
    app,
    prompt1|llm_gemma,
    path="/essay"
)

add_routes(
    app,
    prompt2|llm_llama,
    path="/poem"
)

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)