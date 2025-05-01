import multiprocessing
import requests
import time
import tracemalloc

urls = [
    'https://tr.wikipedia.org/wiki/T%C3%BCrk_bayra%C4%9F%C4%B1#/media/Dosya:Flag_of_Turkey.svg',
    'https://tr.wikipedia.org/wiki/Linux#/media/Dosya:Tux.svg',
    'https://tr.wikipedia.org/wiki/Microsoft#/media/Dosya:Building_92_of_Microsoft_Redmond_Campus_-_panoramio.jpg'
]

def download_file(url, index):
    response = requests.get(url, timeout=30)
    with open(f'process_file_{index}.bin', 'wb') as f:
        f.write(response.content)
    print(f'Process {index} finished downloading.')

if __name__ == '__main__':
    tracemalloc.start()
    start_time = time.time()

    processes = []
    for i, url in enumerate(urls):
        p = multiprocessing.Process(target=download_file, args=(url, i))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Multiprocessing total time: {end_time - start_time:.2f} seconds")
    print(f"Peak memory usage: {peak / (1024 ** 2):.2f} MB")
