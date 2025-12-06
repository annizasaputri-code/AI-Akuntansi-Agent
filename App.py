import streamlit as st
from langchain.chat_models import ChatGroq
from langchain.chains import ConversationChain
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Model
model = ChatGroq(groq_api_key=api_key, model_name="llama-3.1-70b-versatile")

# Agent / Chat Memory
conversation = ConversationChain(llm=model)

# UI Streamlit
st.title("🤖 AI Agent Akuntansi")
st.write("Tanya apa aja tentang akuntansi — jurnal, laporan, rasio, dll ✨")

user_input = st.text_input("Masukkan pertanyaan kamu:")

if user_input:
    response = conversation.predict(input=user_input)
    st.success(response)
