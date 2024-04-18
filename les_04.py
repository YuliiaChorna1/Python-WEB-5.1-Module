# parallel tasks execution

import asyncio
import random

async def random_value():
    print("Start task")
    await asyncio.sleep(1)
    print("Task finished")
    return random.random()

async def main():
    tasks = []
    print("Task scheduled")

    for _ in range(3):
        tasks.append(asyncio.create_task(random_value()))

    print("Sleep time")
    await asyncio.sleep(2)
    print("Sleep over")

    for task in tasks:
        print("Awaiting")
        await task
        print(f"result: {task.result()}")

if __name__ == '__main__':
    asyncio.run(main())

