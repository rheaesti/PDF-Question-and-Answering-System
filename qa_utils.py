from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv
import os
import google.generativeai as genai  # Gemini SDK

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Initialize Gemini
genai.configure(api_key=gemini_api_key)
gemini_model = genai.GenerativeModel("gemini-2.0-flash")

def chunk_text(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return splitter.split_text(text)

def store_chunks_in_vectordb(chunks):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectordb = Chroma.from_texts(chunks, embedding=embeddings)
    return vectordb

def get_answer_from_query(vectordb, query):
    docs = vectordb.similarity_search(query)
    context = "\n\n".join([doc.page_content for doc in docs])
    
    prompt = f"""Answer the following question based on the context below:

Context:
{context}

Question:
{query}
"""
    response = gemini_model.generate_content(prompt)
    return response.text
