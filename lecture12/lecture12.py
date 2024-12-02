import random
import time

def create_file(filename):
    with open(filename, "w") as file:
        for _ in range(100):
            line = " ".join(str(random.randint(1, 100)) for _ in range(20))
            file.write(line + "\n")

def process_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    processed_lines = []
    for line in lines:
        numbers = list(map(int, line.split()))
        filtered_numbers = list(filter(lambda x: x > 40, numbers))
        processed_lines.append(filtered_numbers)
    return processed_lines

def write_processed_file(filename, data):
    with open(filename, "w") as file:
        for line in data:
            file.write(" ".join(map(str, line)) + "\n")

def read_file_as_generator(filename):
    with open(filename, "r") as file:
        for line in file:
            yield list(map(int, line.split()))

def execution_time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@execution_time_decorator
def main():
    filename = "numbers.txt"
    create_file(filename)
    processed_data = process_file(filename)
    write_processed_file(filename, processed_data)
    for line in read_file_as_generator(filename):
        print(line)

main()
