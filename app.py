import streamlit as st
from agent import ask_banking_agent
from glossary_rag import ask_glossary_qa
from calculator import calculate_interest
import PyPDF2

st.set_page_config(page_title="BFSIHelper AI", layout="wide")
st.title("💳📊 BFSIHelper AI – Smart Banking & Finance Agent")

st.header("📤 Upload Your Financial PDF")
pdf = st.file_uploader("Upload bank statement or glossary PDF", type=["pdf"])
if pdf:
    reader = PyPDF2.PdfReader(pdf)
    raw_text = "\n".join([page.extract_text() for page in reader.pages])
    st.text_area("📃 Extracted Text", raw_text, height=200)

st.divider()
st.subheader("🤖 Ask BFSI Agent (Ollama)")
user_q = st.text_input("Ask something (e.g., What is repo rate?)")
if user_q:
    response = ask_banking_agent(user_q)
    st.markdown(response)

st.divider()
st.subheader("📚 Ask Glossary-Based Question (RAG)")
rag_q = st.text_input("Ask from uploaded glossary PDF")
if rag_q and pdf:
    st.markdown(ask_glossary_qa(pdf, rag_q))

st.divider()
st.subheader("🧮 Loan Interest Calculator")
p = st.number_input("Principal", min_value=1000)
r = st.number_input("Annual Interest Rate (%)", min_value=1.0)
t = st.number_input("Time (years)", min_value=1)
if st.button("Calculate"):
    st.success(f"Total Simple Interest = ₹{calculate_interest(p, r, t)}")
