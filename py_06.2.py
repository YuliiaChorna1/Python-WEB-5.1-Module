# паралельне виконання py_06.1.py (requests)

# Ми робимо функцію обгортку preview_fetch_async над функцією preview_fetch.
# Всередині беремо поточний виконуваний Event loop loop = asyncio.get_running_loop() та 
# за допомогою ThreadPoolExecutor поміщаємо функцію preview_fetch в Executor:
# [loop.run_in_executor(pool, preview_fetch, url) for url in urls]. 
# Отриманий список об'єктів Futures передаємо в asyncio.gather(*futures) 
# для отримання остаточного результату.

import asyncio
import requests
from time import time
from concurrent.futures import ThreadPoolExecutor

urls = ["http://www.google.com", "http://www.python.org", "http://duckduckgo.com"]

def preview_fetch(url):
    r = requests.get(url)
    return url, r.text[:150]


async def preview_fetch_async():
    loop = asyncio.get_running_loop()

    with ThreadPoolExecutor(3) as pool:
        futures = [loop.run_in_executor(pool, preview_fetch, url) for url in urls]
        result = await asyncio.gather(*futures, return_exceptions=True)
        return result
    
if __name__ == '__main__':
    start = time()
    r = asyncio.run(preview_fetch_async())
    print(r)
    print(time() - start)
