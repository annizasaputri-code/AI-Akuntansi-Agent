import streamlit as st
from langchain_groq import ChatGroq
from langchain.chains import ConversationChain
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

model = ChatGroq(api_key=api_key, model_name="llama-3.1-70b-versatile")
conversation = ConversationChain(llm=model)

st.title("🤖 AI Agent Akuntansi")
st.write("Tanya tentang jurnal, laporan keuangan, rasio, SAP/PSAK, dan lainnya 💬✨")

user_input = st.text_input("Tanyakan sesuatu:")

if user_input:
    response = conversation.predict(input=user_input)
    st.success(response)
