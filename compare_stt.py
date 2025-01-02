import requests
import time
import matplotlib.pyplot as plt

# Define the endpoints
CPU_URL = "http://localhost:5001/transcribe"
GPU_URL = "http://localhost:5002/transcribe"

# Audio file(s) for testing
audio_files = [
    "path/to/audio1.mp3",  # Short file
    "path/to/audio2.wav",  # Medium file
    "path/to/audio3.flac", # Long file
]

# Function to test an endpoint
def test_endpoint(url, file_path):
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
def run_tests():
    results = {"cpu": [], "gpu": []}

    for file_path in audio_files:
        print(f"Testing file: {file_path}")
        
        # Test CPU
        cpu_time, cpu_result = test_endpoint(CPU_URL, file_path)
        print(f"CPU: {cpu_time}s, Result: {cpu_result}")
        results["cpu"].append(cpu_time)
        
        # Test GPU
        gpu_time, gpu_result = test_endpoint(GPU_URL, file_path)
        print(f"GPU: {gpu_time}s, Result: {gpu_result}")
        results["gpu"].append(gpu_time)

    return results

# Plot results
def plot_results(results):
    labels = [f"File {i+1}" for i in range(len(audio_files))]
    cpu_times = results["cpu"]
    gpu_times = results["gpu"]

    x = range(len(labels))
    plt.figure(figsize=(10, 6))
    plt.bar(x, cpu_times, width=0.4, label="CPU", align="center", color="blue")
    plt.bar(x, gpu_times, width=0.4, label="GPU", align="edge", color="green")
    plt.xticks(x, labels)
    plt.xlabel("Audio Files")
    plt.ylabel("Processing Time (s)")
    plt.title("CPU vs GPU Transcription Time")
    plt.legend()
    plt.show()

# Main execution
if __name__ == "__main__":
    test_results = run_tests()
    plot_results(test_results)
