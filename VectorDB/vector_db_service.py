from flask import Flask, request, jsonify
import faiss
import numpy as np

app = Flask(__name__)

# Initialize FAISS index
index = faiss.IndexFlatL2(768)  # Adjust dimension based on your model

@app.route('/store', methods=['POST'])
def store_vector():
    vector = request.json.get('vector')
    vector = np.array(vector).astype('float32')
    index.add(vector)
    return jsonify({"status": "success"})

@app.route('/search', methods=['POST'])
def search_vector():
    query_vector = request.json.get('vector')
    query_vector = np.array(query_vector).astype('float32')
    k = request.json.get('k', 5)  # Number of nearest neighbors to return
    D, I = index.search(query_vector, k)
    return jsonify({"distances": D.tolist(), "indices": I.tolist()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)