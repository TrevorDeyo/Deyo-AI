import requests

# URL of the DeepSeek service exposed by nginx
url = "http://localhost/deepseek/chat"

# Sample data to send to the DeepSeek service
data = {
    "messages": [
        {"role": "user", "content": "Hello, how are you?"},
        {"role": "assistant", "content": "I'm good, thank you! How can I help you today?"},
        {"role": "user", "content": "What is the capital of France?"}
    ]
}

# Send a POST request with the sample data
try:
    response = requests.post(url, json=data)
    response.raise_for_status()  # Raise an exception for bad status codes

    # Parse the JSON response
    response_data = response.json()
    print("Response:", response_data.get("response"))
except requests.exceptions.RequestException as e:
    print(f"Error connecting to the service: {e}")
except ValueError:
    print("Error decoding JSON response.")
    print("Raw response:", response.text)
except Exception as e:
    print(f"An unexpected error occurred: {e}")