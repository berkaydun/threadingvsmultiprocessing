import multiprocessing
import time
import tracemalloc


def returnPrimes(n):
    primes = []
    for num in range(2, n):
        prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                prime = False
                break
        if prime:
            primes.append(num)
    return primes


def main():
    primes = [93719, 93911, 99371]
    processes = []

    tracemalloc.start()
    start_time = time.time()

    for prime in primes:
        process = multiprocessing.Process(target=returnPrimes, args=(prime,))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Time taken  : {end_time - start_time:.2f} seconds")
    print(f"{current / (1024 ** 2):.2f} MB current memory usage, {peak / (1024 ** 2):.2f} MB peak memory usage")


if __name__ == "__main__":
    main()
