import requests
import time
import matplotlib.pyplot as plt
import os

# Define the GPU endpoint
GPU_URL = "http://localhost:5002/transcribe"

# Audio file(s) for testing
audio_files = [
    r"C:\Users\tdeyo\Desktop\Code\DeyoAI\TestShort.mp3",  # Short file
    r"C:\Users\tdeyo\Desktop\Code\DeyoAI\TestMedium.mp3",  # Medium file
    r"C:\Users\tdeyo\Desktop\Code\DeyoAI\TestLong.mp3", # Long file
]

# Function to test the GPU endpoint
def test_gpu_endpoint(url, file_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return None, {"error": "File not found"}

    with open(file_path, "rb") as audio_file:
        files = {"file": audio_file}
        start_time = time.time()
        try:
            response = requests.post(url, files=files)
            elapsed_time = time.time() - start_time
            if response.status_code == 200:
                return elapsed_time, response.json()
            else:
                return elapsed_time, {"error": response.text}
        except requests.exceptions.RequestException as e:
            return None, {"error": str(e)}

# Run tests and collect results
def run_gpu_tests():
    results = []

    for file_path in audio_files:
        print(f"Testing file: {file_path}")
        
        # Test GPU
        gpu_time, gpu_result = test_gpu_endpoint(GPU_URL, file_path)
        if gpu_time is not None:
            print(f"GPU: {gpu_time}s, Result: {gpu_result}")
            results.append(gpu_time)
        else:
            print(f"Error testing file {file_path}: {gpu_result['error']}")

    return results

# Plot results
def plot_gpu_results(results):
    labels = [f"File {i+1}" for i in range(len(audio_files))]
    gpu_times = results

    x = range(len(labels))
    plt.figure(figsize=(10, 6))
    plt.bar(x, gpu_times, width=0.4, label="GPU", align="center", color="green")
    plt.xticks(x, labels)
    plt.xlabel("Audio Files")
    plt.ylabel("Processing Time (s)")
    plt.title("GPU Transcription Time")
    plt.legend()
    plt.show()

# Main execution
if __name__ == "__main__":
    gpu_test_results = run_gpu_tests()
    plot_gpu_results(gpu_test_results)