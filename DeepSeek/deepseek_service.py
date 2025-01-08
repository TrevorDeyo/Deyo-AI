from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

openai_client = openai.Client(
    base_url="http://localhost:30000/v1",  # Assuming SGLang server is on localhost
    api_key="EMPTY"
)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    messages = data.get('messages', [])

    try:
        response = openai_client.chat.completions.create(
            model="default",
            messages=messages,
            temperature=0.7,
            max_tokens=200
        )
        return jsonify({"response": response.choices[0].message.content})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # This is only for local testing, Gunicorn will handle deployment
    app.run(debug=True, host='0.0.0.0', port=5000)