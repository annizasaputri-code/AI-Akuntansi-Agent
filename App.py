import streamlit as st
from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain.chains import LLMChain

# Load API Key
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Model
model = ChatGroq(api_key=api_key, model_name="llama-3.1-70b-versatile")

# Prompt (biar AI fokus akuntansi)
prompt = PromptTemplate(
    input_variables=["question"],
    template="""
Kamu adalah AI yang ahli dalam akuntansi, terutama PSAK, SAP, jurnal, laporan keuangan, analisis rasio, akuntansi pemerintahan, dan perpajakan.

Jawab dengan jelas, sederhana, dan contoh jika perlu.

Pertanyaan user: {question}
"""
)

chain = LLMChain(llm=model, prompt=prompt)

# UI Streamlit
st.title("📊 AI Accounting Assistant")
st.write("Silakan tanya tentang akuntansi apa pun ✨")

question = st.text_input("Masukkan pertanyaan:")

if question:
    answer = chain.run(question)
    st.success(answer)
