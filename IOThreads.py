import threading
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
    with open(f'thread_file_{index}.bin', 'wb') as f:
        f.write(response.content)
    print(f'Thread {index} finished downloading.')

tracemalloc.start()
start_time = time.time()

threads = []
for i, url in enumerate(urls):
    t = threading.Thread(target=download_file, args=(url, i))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end_time = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Threading total time: {end_time - start_time:.2f} seconds")
print(f"Peak memory usage: {peak / (1024 ** 2):.2f} MB")
