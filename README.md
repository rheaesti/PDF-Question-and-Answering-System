# PDF-Question-and-Answering-System
# PDF Q&A App

A Streamlit-based web application that allows users to **upload a PDF document and ask questions** about its content using natural language. It combines **PDF parsing**, **text chunking**, **semantic vector search**, and **Google Gemini generative AI** to provide intelligent, context-aware answers.

---

## Features

- Upload and parse PDF documents
- Chunk large text content using `LangChain`
- Embed content with `HuggingFace Transformers`
- Store embeddings in `Chroma` vector DB
- Use **Google Gemini** to answer questions
- Interactive Streamlit interface

---

## How It Works

1. **PDF Upload**: Users upload a PDF via the web interface.
2. **Text Extraction**: Text is extracted using `pdfplumber`.
3. **Chunking**: The text is split into overlapping chunks with `RecursiveCharacterTextSplitter`.
4. **Embedding**: Chunks are converted into embeddings using `all-MiniLM-L6-v2`.
5. **Vector Storage**: Embeddings are stored in Chroma for semantic search.
6. **Q&A**: User questions are matched against the most relevant chunks, and **Gemini** generates a natural language answer.

---

## Tech Stack

| Layer            | Tools/Libs                         |
|------------------|------------------------------------|
| Frontend         | Streamlit                          |
| PDF Processing   | pdfplumber                         |
| Text Splitting   | LangChain                          |
| Embedding Model  | sentence-transformers/all-MiniLM-L6-v2 |
| Vector DB        | Chroma                             |
| LLM API          | Google Gemini via `google.generativeai` |
| Environment      | Python 3.10+, `.env` for API keys  |

---

## Project Structure

```bash
├── app.py                  # Streamlit App
├── pdf_utils.py           # PDF Text Extraction
├── qa_utils.py            # Chunking, Vector DB, LLM Response
├── requirements.txt       # Python dependencies
└── .env                   # GEMINI_API_KEY here
