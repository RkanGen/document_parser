import spacy
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.schema import Document
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Load spaCy model for NER
nlp = spacy.load("en_core_web_sm")

def entity_recognition(text):
    doc = nlp(text)
    entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]
    return entities

def get_embeddings(text):
    # Initialize OpenAI embeddings via LangChain
    openai_api_key = os.getenv("OPENAI_API_KEY")
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    doc = Document(page_content=text)
    embedded_doc = embeddings.embed_documents([doc])
    return embedded_doc
