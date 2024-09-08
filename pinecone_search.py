import pinecone
import os
from dotenv import load_dotenv
from nlp import get_embeddings

# Load environment variables
load_dotenv()

# Initialize Pinecone
pinecone_api_key = os.getenv("PINECONE_API_KEY")
pinecone.init(api_key=pinecone_api_key, environment="us-west1-gcp")
index = pinecone.Index("document-parser")

class PineconeHandler:
    def __init__(self):
        self.index = index

    def store_embeddings(self, doc_id, embeddings):
        self.index.upsert(vectors=[(doc_id, embeddings)])

    def search_embeddings(self, query_text):
        query_embeddings = get_embeddings(query_text)
        search_results = self.index.query(queries=query_embeddings, top_k=5)
        return search_results
