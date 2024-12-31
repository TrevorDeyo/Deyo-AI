import whisper
from flask import Flask, request, jsonify

app = Flask(__name__)
model = whisper.load_model("base")

@app.route('/transcribe', methods=['POST'])
def transcribe():
    audio_file = request.files['file']
    result = model.transcribe(audio_file)
    return jsonify({'text': result['text']})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
