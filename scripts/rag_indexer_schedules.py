import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app, db
from app.models import Itinerary, Schedule, Activity
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
import shutil

openai_api_key = os.getenv("OPENAI_API_KEY")

# Remove old index if it exists
if os.path.exists("faiss_index_activities"):
    shutil.rmtree("faiss_index_activities")

with app.app_context():
    all_chunks = []

    itineraries = Itinerary.query.all()
    for itinerary in itineraries:
        title = itinerary.title
        for schedule in itinerary.schedule:
            day = schedule.day
            activities = schedule.activity

            if not activities:
                continue

            activity_lines = []
            for activity in activities:
                if activity.place and activity.description:
                    activity_lines.append(f"- {activity.place}: {activity.description}")

            if activity_lines:
                chunk = f"Itinerary: {title}\nDay: {day}\n" + "\n".join(activity_lines)
                all_chunks.append(chunk)

    # Split (if needed)
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    split_chunks = []
    for text in all_chunks:
        split_chunks.extend(splitter.split_text(text))

    embedder = OpenAIEmbeddings(openai_api_key=openai_api_key)
    vectorstore = FAISS.from_texts(split_chunks, embedder)
    vectorstore.save_local("faiss_index_activities")

    print("✅ Structured itinerary schedule index saved.")
