import asyncio
import random


async def random_value():
    print("Start task")
    await asyncio.sleep(1)
    print("Task is finished")
    return random.random()

async def main():
    task = asyncio.create_task(random_value())
    print("Task is scheduled")
    await task
    print(f"result: {task.result()}")


if __name__ == '__main__':
    asyncio.run(main())

