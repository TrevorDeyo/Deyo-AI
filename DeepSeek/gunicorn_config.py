import multiprocessing

# Calculate the number of workers based on the number of CPU cores
workers = min((multiprocessing.cpu_count() * 2) + 1, 2)  # Limit to a maximum of 2 workers

# Gunicorn configuration
bind = "0.0.0.0:5000"
timeout = 120
