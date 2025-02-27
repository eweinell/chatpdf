import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import ConversationalRetrievalChain
from langchain_ollama.llms import OllamaLLM
from src.ui import PDFChatbot
import logging

class App:
    def __init__(self):
        """Initialize the application and set up the UI."""
        self.ui = PDFChatbot(self.tokenize_pdf, self.initialize_chat_engine)
        logging.basicConfig(level=logging.INFO)

    def tokenize_pdf(self, file):
        """Tokenize the text of a PDF file into chunks.

        Args:
            file: A file object representing the PDF.

        Returns:
            Tuple containing the list of text chunks and the number of chunks.
        """
        try:
            pdf = PdfReader(file)
            text = ""
            for page in pdf.pages:
                text += page.extract_text()
            
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
            chunks = text_splitter.split_text(text)
            
            return chunks, len(chunks)
        except Exception as e:
            logging.error(f"Error tokenizing PDF: {e}")
            raise

    def initialize_chat_engine(self, chunks):
        """Initialize the chat engine with the given text chunks.

        Args:
            chunks: List of text chunks.

        Returns:
            ConversationalRetrievalChain object.
        """
        try:
            embeddings = OllamaEmbeddings(model="pdf-analyzer")
            vectorstore = Chroma.from_texts(chunks, embeddings)
            
            llm = OllamaLLM(model="pdf-analyzer")
            qa_chain = ConversationalRetrievalChain.from_llm(llm, vectorstore.as_retriever())
            
            return qa_chain
        except Exception as e:
            logging.error(f"Error initializing chat engine: {e}")
            raise
    
    def run(self):
        """Run the application."""
        self.ui.run()