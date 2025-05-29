from flask import Blueprint, request, jsonify
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
import http.client
import json
import os

ai_routes = Blueprint('ai', __name__)

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')


@ai_routes.route('/recommendations', methods=['POST'])
def get_travel_recommendations():
    data = request.json
    user_query = data.get('query', '')

    # Setup connection
    conn = http.client.HTTPSConnection("api.openai.com")

    # Set headers
    headers = {
        'Authorization': f'Bearer {OPENAI_API_KEY}',
        'Content-Type': 'application/json'
    }

    # Define the payload
    payload = json.dumps({
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a travel assistant."},
            {"role": "user", "content": user_query}
        ]
    })

    try:
        # Send the POST request
        conn.request("POST", "/v1/chat/completions", payload, headers)

        # Get the response
        response = conn.getresponse()
        data = response.read()

        # Parse and return the JSON response
        response_json = json.loads(data.decode("utf-8"))
        return jsonify(response_json), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()


@ai_routes.route("/schedule", methods=["POST"])
def get_itinerary_schedule():
    data = request.json
    itinerary_title = data.get("title")

    if not itinerary_title:
        return jsonify({"error": "Missing itinerary title"}), 400

    try:
        embedder = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
        vectorstore = FAISS.load_local("faiss_index_activities", embedder, allow_dangerous_deserialization=True)

        docs = vectorstore.similarity_search(itinerary_title, k=4)
        context = "\n\n".join([doc.page_content for doc in docs])

        prompt = f"""
You are a helpful travel assistant. Based ONLY on the context below, extract a concise summary of the daily schedule for this itinerary: "{itinerary_title}".

⚠️ Format each line like this:
Day 1: [Main locations/activities]
Day 2: [Main locations/activities]
...

Only use content from the context. Do not invent or add anything not mentioned in the context. If a day number is not clearly labeled, infer the order from top to bottom.


Context:
{context}

Answer with a clear daily itinerary plan:
"""

        # Prepare OpenAI API request
        conn = http.client.HTTPSConnection("api.openai.com")
        headers = {
            'Authorization': f'Bearer {OPENAI_API_KEY}',
            'Content-Type': 'application/json'
        }

        payload = json.dumps({
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": "You are a helpful travel assistant."},
                {"role": "user", "content": prompt}
            ]
        })

        conn.request("POST", "/v1/chat/completions", body=payload, headers=headers)
        response = conn.getresponse()
        response_data = response.read()
        response_json = json.loads(response_data.decode("utf-8"))
        conn.close()

        # Return the generated schedule
        schedule_text = response_json.get("choices", [{}])[0].get("message", {}).get("content", "No schedule generated.")
        return jsonify({"schedule": schedule_text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
