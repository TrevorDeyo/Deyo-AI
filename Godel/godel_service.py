from flask import Flask, request, jsonify
import godel

app = Flask(__name__)
model = godel.load_model("base")  # Load the GODEL model

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get("prompt")
    
    # Generate response using GODEL
    response = model.generate(prompt)
    
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)