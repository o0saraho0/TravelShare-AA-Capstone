import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app, db
from app.models.itinerary import Itinerary

from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import openai

# Load env variables
openai.api_key = os.getenv("OPENAI_API_KEY")

with app.app_context():
    # Step 1: Fetch data
    itineraries = Itinerary.query.all()
    documents = [item.description for item in itineraries if item.description]

    # Step 2: Chunk text
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = []
    for doc in documents:
        chunks.extend(splitter.split_text(doc))

    # Step 3: Embed and save
    embedder = OpenAIEmbeddings(openai_api_key=openai.api_key)
    vectorstore = FAISS.from_texts(chunks, embedder)
    vectorstore.save_local("faiss_index")

    print("✅ RAG vector index saved successfully.")
