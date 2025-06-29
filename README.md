# JE29-BFSIHelper-AI
GEN AI

💳📊 BFSIHelper AI – Personalized Banking & Finance Support Agent
🧠 Project Idea
BFSIHelper AI is a smart agent designed to assist users with basic banking and finance-related queries. It works offline using Ollama (TinyLLaMA or Mistral), processes documents (like account statements, credit reports, or terms and conditions), and answers user questions about:

Banking terms

Loan eligibility

Credit card policies

Interest calculations

Insurance FAQs

🔑 Core Features
Feature	Description
📄 Upload PDF Statements	Users upload their bank or credit statements (PDF)
🤖 Ask BFSI Agent (Ollama)	Ask questions like "Am I eligible for a home loan?"
📜 Explain Financial Terms	Ask "Explain EMI vs SIP" or "What is a ULIP?"
🧮 Interest Calculator (Bonus)	Built-in loan/FD interest calculator
📚 Smart Glossary Agent	RAG-enabled agent to answer from uploaded BFSI terms document

📘 README.md
markdown
Copy
Edit
# 💳📊 BFSIHelper AI – Smart Banking & Finance Assistant

An AI app built using Python, Streamlit, and Ollama to:
- Answer user queries related to BFSI
- Process PDFs like statements or glossary
- Calculate loan/FD interest
- Use RAG for glossary-based queries

## 🚀 How to Run

```bash
git clone https://github.com/yourusername/BFSIHelper-AI.git
cd BFSIHelper-AI
pip install -r requirements.txt
ollama serve
ollama run tinyllama
streamlit run app.py
