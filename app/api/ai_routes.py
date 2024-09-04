from flask import Blueprint, request, jsonify
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
