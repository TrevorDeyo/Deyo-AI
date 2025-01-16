from flask import Flask, request, jsonify
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM

app = Flask(__name__)

# Initialize the pipeline
pipe = pipeline("text-generation", model="microsoft/phi-4", trust_remote_code=True)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    messages = data.get("messages", [])
    result = pipe(messages)
    return jsonify(result)

@app.route('/load_model', methods=['GET'])
def load_model():
    tokenizer = AutoTokenizer.from_pretrained("microsoft/phi-4", trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained("microsoft/phi-4", trust_remote_code=True)
    return jsonify({"status": "Model loaded successfully"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6000)