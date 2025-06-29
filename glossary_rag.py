from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain_community.llms.ollama import Ollama
from langchain.text_splitter import CharacterTextSplitter

def ask_glossary_qa(file, question):
    loader = PyPDFLoader(file.name)
    pages = loader.load_and_split()
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = splitter.split_documents(pages)
    embed = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = FAISS.from_documents(texts, embed)
    retriever = db.as_retriever()
    llm = Ollama(model="tinyllama")
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa.run(question)
