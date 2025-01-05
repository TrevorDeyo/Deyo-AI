import requests

# URL of the Flask app running inside the Docker container
url = "http://localhost:5001/transcribe"

# Path to the audio file you want to transcribe
audio_file_path = r"C:\Users\tdeyo\Desktop\Code\DeyoAI\TestShort.mp3"  # Replace with the path to your audio file

# Open the audio file in binary mode
with open(audio_file_path, 'rb') as audio_file:
    # Send a POST request with the audio file
    files = {'file': audio_file}
    response = requests.post(url, files=files)

# Check the response
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    print("Transcription:", data["text"])
else:
    print(f"Error: {response.status_code}")
    print("Response:", response.text)
