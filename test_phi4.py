import requests

url = "http://localhost:6000/generate"
data = {
    "messages": [
        {"role": "user", "content": "Who are you?"}
    ]
}

response = requests.post(url, json=data)
if response.status_code == 200:
    print("Response:", response.json())
else:
    print("Error:", response.status_code, response.text)