import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_community.llms import ollama

## Langsmit Tracking
# os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
import os

langchain_api_key = os.getenv("LANGCHAIN_API_KEY")

if langchain_api_key:
    os.environ["LANGSMITH_API_KEY"] = langchain_api_key
else:
    print("LANGCHAIN_API_KEY is not configured.")

LANGSMITH_TRACING='true'
LANGSMITH_API_KEY=langchain_api_key
LANGSMITH_PROJECT='LangChain_Practice'


## Prompt Templates

prompts = ChatPromptTemplate.from_messages(
    [
        ("system","You are healpfull assistance for user. Please response accourding to user query"),
        ("user","Questions : {question}")
    ]
)


## Generate response
def generate_response(user_inpute, api_key, temperature, max_token):
    llm = ChatOllama(
        model="llama3.2:3b",
        temperature=temperature,
        num_predict=max_token
    )

    response = llm.invoke(user_inpute)
    return response.content

# Title of the app

st.title("Q and A Chatbot")
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your api key", type="password")

# dropdown sleect open ai model

llm = st.sidebar.selectbox("Select model for the response",["llama3.2:3b"])

max_token = st.sidebar.slider("Max_Token", min_value=50, max_value=250, value=100 )

temperature = st.sidebar.slider("teamperature",min_value=0.0, max_value=1.0, value=0.7)

## Main Interface

st.write("Ask your question")
st.write("Selected Model is :",llm)
user_inpute = st.text_input("You")

if user_inpute:
    response = generate_response(
    user_inpute,
    api_key,
    temperature,
    max_token
)
    st.write(response)
else:
    st.write("Please provide your query")



from langchain_ollama import OllamaLLM

llm = OllamaLLM(
    model="llama3.2:3b",
    temperature=temperature
)

response = llm.invoke(user_inpute)
print("LANGCHAIN_API_KEY is not configured.")

st.write(response)