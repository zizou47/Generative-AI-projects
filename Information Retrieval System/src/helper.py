import os
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import GooglePalmEmbeddings
from langchain.llms import google_Palm
from langchain.vectorstores import FAISS
from langchain.chains import Conversational_Retrieval
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv


load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
os.environ['GOOGLE_API_KEY'] =  GOOGLE_API_KEY



def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
         pdf_reader = PdfReader(pdf_docs)
         for page in pdf_reader.pages:
              text += page.extract_text()
    return text

def get_text_chunks(text):
     text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 20)
     chunks = text_splitter.split_text(text)
     return chunks


def get_vector_store(text_chunks):
     embeddings = GooglePalmEmbeddings()
     
