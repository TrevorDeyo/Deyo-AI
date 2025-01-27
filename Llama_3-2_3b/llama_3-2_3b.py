from flask import Flask, request, jsonify
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Initialize the pipeline with LLaMA model
logging.info("Initializing the pipeline...")
pipe = pipeline("text-generation", model="facebook/llama-3.23b", trust_remote_code=True)
logging.info("Pipeline initialized.")

@app.route('/generate', methods=['POST'])
def generate():
    logging.info("Received request at /generate endpoint.")
    data = request.json
    messages = data.get("messages", [])
    result = pipe(messages)
    logging.info("Generated response.")
    return jsonify(result)

@app.route('/load_model', methods=['GET'])
def load_model():
    logging.info("Received request at /load_model endpoint.")
    tokenizer = AutoTokenizer.from_pretrained("facebook/llama-3.23b", trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained("facebook/llama-3.23b", trust_remote_code=True)
    logging.info("Model loaded successfully.")
    return jsonify({"status": "Model loaded successfully"})

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    logging.info("Starting Flask application...")
    app.run(host='0.0.0.0', port=7000)