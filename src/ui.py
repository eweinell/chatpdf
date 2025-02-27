from typing import Tuple, List, Any, Callable, Dict
import streamlit as st
from streamlit.runtime import uploaded_file_manager as stfm
from PIL import Image



class PDFChatbot:
    def __init__(self, tokenize: Callable[[Any, stfm.UploadedFile], Tuple[List[str],int]], initChat: Callable[[Any, Any], Any]):
        self.conversation_id = None
        self.title = "PDF Chatbot using Mistral 22B"
        self.uploaded_file = None
        self.tokenize = tokenize
        self.initChat = initChat

    def _title(self):
        st.title(self.title)
        
    def _uploaded_file(self, file_uploader="Choose a PDF file"):
        if file_uploader is not None:
            file = st.file_uploader(file_uploader, type="pdf")
            return file
        
    def _display_messages(self):
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    def _post_message(self, role: str, message: str):
        st.session_state.messages.append({"role":role, "content": message})
        with st.chat_message(role):
            st.markdown(message)

    def _chat_input(self, prompt="Ask about the PDF"):
        self._display_messages()
        if (user_input := st.chat_input(prompt)) is not None:
            self._post_message("user", user_input)
            hist = PDFChatbot._format_chat_history(st.session_state.messages)
            response = st.session_state.qa_chain({"question": user_input, "chat_history": hist})
            self._post_message("assistant", response["answer"])

    def run(self):
        if "messages" not in st.session_state:
            st.session_state.messages = []
        st.sidebar.write("Using Mistral 22B model via Ollama")
        uploaded_file = self._uploaded_file()
        if uploaded_file is not None:
            if "chunks" not in st.session_state:
                st.session_state.chunks, st.session_state.token_count = self.tokenize(uploaded_file)
                st.write(f"Document tokenized. Total chunks: {st.session_state.token_count}")
                st.session_state.qa_chain = self.initChat(st.session_state.chunks)
            self._chat_input()

    @staticmethod
    def _format_chat_history(messages: List[Dict[str, str]]) -> List[Tuple[str, str]]:
        return [
            (f"Human: {messages[i]['content']}", f"AI: {messages[i+1]['content']}")
            for i in range(0, len(messages)-1, 2)
            if messages[i]["role"] == "user" and messages[i+1]["role"] == "assistant"
        ]