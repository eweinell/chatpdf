import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import ConversationalRetrievalChain
from langchain_ollama.llms import OllamaLLM
from src.ui import PDFChatbot

class App:
    def __init__(self):
        self.ui = PDFChatbot(self.tokenize_pdf, self.initialize_chat_engine)

    def tokenize_pdf(self, file):
        pdf = PdfReader(file)
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
        
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = text_splitter.split_text(text)
        
        return chunks, len(chunks)

    def initialize_chat_engine(self, chunks):
        embeddings = OllamaEmbeddings(model="pdf-analyzer")
        vectorstore = Chroma.from_texts(chunks, embeddings)
        
        llm = OllamaLLM(model="pdf-analyzer")
        qa_chain = ConversationalRetrievalChain.from_llm(llm, vectorstore.as_retriever())
        
        return qa_chain
    
    def run(self):
        self.ui.run()


