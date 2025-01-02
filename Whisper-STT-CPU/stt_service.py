from flask import Flask, request, jsonify
import whisper
import torch

print(f"Is CUDA available? {torch.cuda.is_available()}")
print(f"Using device: {torch.cuda.current_device()}")

app = Flask(__name__)
model = whisper.load_model("base")  # You can change this to other models like "large" if needed

@app.route('/transcribe', methods=['POST'])
def transcribe():
    file = request.files['file']
    audio_path = "/tmp/audio.wav"
    file.save(audio_path)
    
    # Transcribe the audio using Whisper
    result = model.transcribe(audio_path)
    
    # Return the transcription result
    return jsonify({"text": result["text"]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
