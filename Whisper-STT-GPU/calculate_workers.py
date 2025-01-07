import multiprocessing

def calculate_workers():
    return (multiprocessing.cpu_count() * 2) + 1

if __name__ == "__main__":
    print(calculate_workers())