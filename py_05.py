# приклад, де у нас є синхронна функція blocks, яка виконує важкі обчислення

# Щоб здійснити блокуючий виклик в Event loop, ми розміщуємо його в Executor 
# і тоді виклик виконується в окремому потоці або процесі.
# У разі, коли основна частина коду – асинхронна (у нашому випадку це функція monitoring)
# і лише окремий виклик блокує увесь Event loop ( функція blocks), 
# такий спосіб перетворити блокуючу функцію на асинхронну цілком виправданий.

# Сам процес перетворення синхронного коду в асинхронний досить простий. 
# Ми обгортаємо функцію blocks функцією run_blocking_tasks.
# Всередині неї беремо окремий loop = asyncio.get_event_loop() та 
# через виклик run_in_executor отримуємо асинхронний результат функції blocks. 
# В якості Executor у нас виступає concurrent.futures.ThreadPoolExecutor

import asyncio
import concurrent.futures
from time import time

def blocks(n):
    counter = n
    start = time()
    while counter > 0:
        counter -= 1
    return time() - start

async def monitoring():
    while True:
        await asyncio.sleep(2)
        print(f"Monitoring {time()}")

async def run_blocking_tasks(executor, n):
    loop = asyncio.get_event_loop()
    print("waiting for executor tasks")
    result = await loop.run_in_executor(executor, blocks, n)
    return result

async def main():
    asyncio.create_task(monitoring())
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        futures = [run_blocking_tasks(executor, n) for n in [50_000_000, 60_000_000, 70_000_000]]
        results = await asyncio.gather(*futures)
        return results
    
if __name__ == '__main__':
    result = asyncio.run(main())
    for r in result:
        print(r)
