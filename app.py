import streamlit as st
from pdf_utils import extract_text_from_pdf
from qa_utils import chunk_text, store_chunks_in_vectordb, get_answer_from_query

st.set_page_config(page_title="PDF Q&A", layout="wide")
st.title("📄 Ask Questions About Your PDF")

pdf_file = st.file_uploader("Upload a PDF", type="pdf")
if pdf_file:
    with st.spinner("Reading and processing your PDF..."):
        text = extract_text_from_pdf(pdf_file)
        chunks = chunk_text(text)
        vectordb = store_chunks_in_vectordb(chunks)
        st.success("PDF processed. Ask your question!")

    query = st.text_input("Ask a question about the PDF")
    if query:
        with st.spinner("Thinking..."):
            answer = get_answer_from_query(vectordb, query)
            st.markdown(f"**Answer:** {answer}")
