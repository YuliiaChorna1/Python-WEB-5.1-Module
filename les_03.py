# Асинхронність - parallel tasks execution

import asyncio


class Task:
    def __init__(self, idx: int) -> None:
        self.idx = idx

    async def run(self) -> None:
        print(f"Task {self.idx} is in progress")
        await asyncio.sleep(1)
        print(f"Task {self.idx} is finished")

async def main():
    tasks = []
    
    for i in range(1, 4):
        task = Task(i)
        tasks.append(task.run()) # не виконує метод run, а додає до списку задач корутину

    await asyncio.gather(*tasks) # кладе усі 3 таски на конвеєр і виконує по черзі поки main на await

    # for task in tasks:  # 1 progress, 1 finished, 2 progress, 2 finished ...
    #     await task

if __name__ == '__main__':
    asyncio.run(main())
