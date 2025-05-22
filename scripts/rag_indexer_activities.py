import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app, db
from app.models import Activity
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from openai import OpenAI

# Set API key
api_key = os.getenv("OPENAI_API_KEY")

# Use Flask app context
with app.app_context():
    # Step 1: Fetch activity descriptions
    activities = Activity.query.all()
    descriptions = [activity.description for activity in activities if activity.description]

    # Step 2: Chunk text
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = []
    for text in descriptions:
        chunks.extend(splitter.split_text(text))

    # Step 3: Embed and save
    embedder = OpenAIEmbeddings(openai_api_key=api_key)
    vectorstore = FAISS.from_texts(chunks, embedder)
    vectorstore.save_local("faiss_index_activities")

    print("✅ Activity-based RAG vector index saved to 'faiss_index_activities'")
