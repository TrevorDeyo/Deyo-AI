FROM lmsysorg/sglang:latest

# Set the working directory
WORKDIR /app

# Copy requirements file and install Python dependencies
COPY requirements.txt . 
RUN pip install -r requirements.txt

# Copy Gunicorn configuration
COPY gunicorn_config.py /app

# Copy the script to calculate workers
COPY calculate_workers.py /app

# Copy your existing application code
COPY . /app

# Expose the SGLang server port (default is 30000)
EXPOSE 30000

# Define the command to start both the SGLang server and Gunicorn
CMD sh -c "python3 -m sglang.launch_server --model deepseek-ai/DeepSeek-V3 --tp 8 --trust-remote-code --port 30000 & gunicorn -c gunicorn_config.py --workers \$(python3 calculate_workers.py) deepseek_service:app"