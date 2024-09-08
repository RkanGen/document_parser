import streamlit as st
from parser import extract_text_from_file
from nlp import entity_recognition, get_embeddings
from pinecone_search import PineconeHandler
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize Pinecone
pinecone_handler = PineconeHandler()

st.title("Efficient Document Parser with Entity Recognition and Search")

# Upload document
uploaded_file = st.file_uploader("Upload a document", type=["pdf", "docx"])

if uploaded_file is not None:
    # Extract and display text
    raw_text = extract_text_from_file(uploaded_file)
    st.subheader("Extracted Text")
    st.write(raw_text)

    # Perform Named Entity Recognition (NER)
    st.subheader("Entity Recognition")
    entities = entity_recognition(raw_text)
    st.json(entities)  # Display detected entities in JSON format

    # Get embeddings for the text
    embeddings = get_embeddings(raw_text)

    # Store embeddings in Pinecone
    pinecone_handler.store_embeddings(uploaded_file.name, embeddings)

    # Search in Pinecone
    query = st.text_input("Search in uploaded documents:")
    if query:
        results = pinecone_handler.search_embeddings(query)
        st.subheader("Search Results")
        st.write(results)
