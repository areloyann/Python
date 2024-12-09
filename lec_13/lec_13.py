import os
import random
import string
import time
from collections import Counter
from threading import Thread, Lock
from multiprocessing import Process, Manager


def generate_large_file(filename, size_in_mb):
    with open(filename, 'w') as f:
        words = [''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 10))) for _ in range(1000)]
        for _ in range(size_in_mb * 1000):  # Rough estimate for ~1MB
            sentence = ' '.join(random.choices(words, k=random.randint(5, 15)))
            f.write(sentence + '\n')


def count_words_sequential(filename):
    word_count = Counter()
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            word_count.update(words)
    return word_count


def count_words_multithreading(filename):
    lock = Lock()
    word_count = Counter()
    threads = []

    def count_chunk(chunk):
        local_counter = Counter()
        for line in chunk:
            words = line.split()
            local_counter.update(words)
        with lock:
            word_count.update(local_counter)

    with open(filename, 'r') as file:
        lines = file.readlines()
        chunk_size = len(lines) // os.cpu_count()
        chunks = [lines[i:i + chunk_size] for i in range(0, len(lines), chunk_size)]

        for chunk in chunks:
            thread = Thread(target=count_chunk, args=(chunk,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    return word_count


def count_words_multiprocessing(filename):
    manager = Manager()
    word_count = manager.dict()
    processes = []

    def count_chunk(chunk, word_count_dict):
        local_counter = Counter()
        for line in chunk:
            words = line.split()
            local_counter.update(words)
        for word, count in local_counter.items():
            word_count_dict[word] = word_count_dict.get(word, 0) + count

    with open(filename, 'r') as file:
        lines = file.readlines()
        chunk_size = len(lines) // os.cpu_count()
        chunks = [lines[i:i + chunk_size] for i in range(0, len(lines), chunk_size)]

        for chunk in chunks:
            process = Process(target=count_chunk, args=(chunk, word_count))
            processes.append(process)
            process.start()

        for process in processes:
            process.join()

    return Counter(word_count)


def measure_time(function, *args):
    start_time = time.time()
    result = function(*args)
    return time.time() - start_time, result


if __name__ == "__main__":
    FILENAME = "large_text_file.txt"
    FILE_SIZE_MB = 10  # Change as needed for testing larger sizes

    print("Generating large file...")
    generate_large_file(FILENAME, FILE_SIZE_MB)

    print("\nMeasuring Sequential Word Counting...")
    sequential_time, sequential_result = measure_time(count_words_sequential, FILENAME)
    print(f"Sequential Time: {sequential_time:.2f} seconds")

    print("\nMeasuring Multithreading Word Counting...")
    multithreading_time, multithreading_result = measure_time(count_words_multithreading, FILENAME)
    print(f"Multithreading Time: {multithreading_time:.2f} seconds")

    print("\nMeasuring Multiprocessing Word Counting...")
    multiprocessing_time, multiprocessing_result = measure_time(count_words_multiprocessing, FILENAME)
    print(f"Multiprocessing Time: {multiprocessing_time:.2f} seconds")

    print("\nResults Summary:")
    print(f"Sequential Time: {sequential_time:.2f} seconds")
    print(f"Multithreading Time: {multithreading_time:.2f} seconds")
    print(f"Multiprocessing Time: {multiprocessing_time:.2f} seconds")
    print(f"Speedup (Multithreading vs Sequential): {sequential_time / multithreading_time:.2f}")
    print(f"Speedup (Multiprocessing vs Sequential): {sequential_time / multiprocessing_time:.2f}")
