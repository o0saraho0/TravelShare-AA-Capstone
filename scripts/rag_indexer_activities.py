import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app, db
from app.models import Schedule, Activity
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from openai import OpenAI

# Set API key
api_key = os.getenv("OPENAI_API_KEY")

# Use Flask app context
with app.app_context():
    schedules = Schedule.query.all()
    day_chunks = []

    for schedule in schedules:
        day = schedule.day
        itinerary_title = schedule.itinerary.title
        activity_texts = []

        for activity in schedule.activity:
            if activity.description:
                activity_texts.append(f"- {activity.place}: {activity.description}")

        if activity_texts:
            day_chunk = f"Itinerary: {itinerary_title}\nDay: {day}\n" + "\n".join(activity_texts)
            day_chunks.append(day_chunk)

    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = []
    for text in day_chunks:
        chunks.extend(splitter.split_text(text))

    embedder = OpenAIEmbeddings(openai_api_key=api_key)
    vectorstore = FAISS.from_texts(chunks, embedder)
    vectorstore.save_local("faiss_index_activities")

    print("✅ Structured itinerary schedule index saved.")