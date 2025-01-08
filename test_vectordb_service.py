import requests
import numpy as np

# URL of the VectorDB service running inside the Docker container
store_url = "http://localhost:5001/store"
search_url = "http://localhost:5001/search"

# Sample vector to store
vector = np.random.rand(768).tolist()  # Replace with your actual vector

# Store the vector
store_response = requests.post(store_url, json={"vector": vector})

# Check the store response
if store_response.status_code == 200:
    print("Vector stored successfully")
else:
    print(f"Error storing vector: {store_response.status_code}")
    print("Response:", store_response.text)

# Sample query vector for searching
query_vector = np.random.rand(768).tolist()  # Replace with your actual query vector

# Search for the nearest neighbors
search_response = requests.post(search_url, json={"vector": query_vector, "k": 5})

# Check the search response
if search_response.status_code == 200:
    search_results = search_response.json()
    print("Search results:", search_results)
else:
    print(f"Error searching vector: {search_response.status_code}")
    print("Response:", search_response.text)