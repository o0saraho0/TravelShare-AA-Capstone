import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from langchain_community.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from openai import OpenAI

# Load your OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Load the embedding model
embedder = OpenAIEmbeddings(openai_api_key=api_key)

# Load the saved FAISS vector index
vectorstore = FAISS.load_local("faiss_index", embedder, allow_dangerous_deserialization=True)

# Ask a question
user_question = "What are some highlights in the Japan itinerary?"

# Retrieve top-k relevant chunks
retrieved_docs = vectorstore.similarity_search(user_question, k=4)

# Build the RAG prompt
context = "\n\n".join([doc.page_content for doc in retrieved_docs])

prompt = f"""
You are a helpful travel assistant. Use the following context to answer the user's question.

Context:
{context}

Question: {user_question}

Answer:
"""

# Send to OpenAI ChatCompletion (v1 API)
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful travel assistant."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.2
)

# Output the response
print("🧠 Answer:\n", response.choices[0].message.content)
