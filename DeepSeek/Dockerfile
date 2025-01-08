FROM lmsysorg/sglang:latest

# Install additional dependencies if needed (beyond what's in the base image)
# RUN apt-get update && apt-get install -y ... && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy your existing application code (if any)
COPY . /app

# Copy Gunicorn configuration
COPY gunicorn_config.py /app

# Copy the script to calculate workers
COPY calculate_workers.py /app

# Define environment variables (if needed)
# ENV MY_VARIABLE=my_value

# Expose the SGLang server port (default is 30000)
EXPOSE 30000

# Define the command to start both the SGLang server and Gunicorn
CMD sh -c "python3 -m sglang.launch_server --model deepseek-ai/DeepSeek-V3 --tp 8 --trust-remote-code --port 30000 & gunicorn -c gunicorn_config.py --workers \$(python3 calculate_workers.py) your_app_module:app"