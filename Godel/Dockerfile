FROM nvidia/cuda:11.2.2-cudnn8-runtime-ubuntu20.04

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Install Godel and Gunicorn
RUN pip3 install godel gunicorn

# Set the working directory
WORKDIR /app

# Copy the application code
COPY . /app

# Copy Gunicorn configuration
COPY gunicorn_config.py /app

# Set the entrypoint
ENTRYPOINT ["gunicorn", "-c", "gunicorn_config.py", "app:app"]
