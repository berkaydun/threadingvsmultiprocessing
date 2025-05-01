import threading
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
    threads = []

    tracemalloc.start()
    start_time = time.time()

    for prime in primes:
        thread = threading.Thread(target=returnPrimes, args=(prime,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Time taken  : {end_time - start_time:.2f} seconds")
    print(f"{current / (1024 ** 2):.2f} MB current mem usage, {peak / (1024 ** 2):.2f} MB peak mem usage")


if __name__ == "__main__":
    main()
