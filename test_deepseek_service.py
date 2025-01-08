import requests

# URL of the DeepSeek service running inside the Docker container
url = "http://localhost:5000/chat"

# Sample data to send to the DeepSeek service
data = {
    "messages": [
        {"role": "user", "content": "Hello, how are you?"},
        {"role": "assistant", "content": "I'm good, thank you! How can I help you today?"}
    ]
}

# Send a POST request with the sample data
response = requests.post(url, json=data)

# Check the response
if response.status_code == 200:
    # Parse the JSON response
    response_data = response.json()
    print("Response:", response_data["response"])
else:
    print(f"Error: {response.status_code}")
    print("Response:", response.text)