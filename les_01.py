# Синхронність

from time import sleep

class Task:
    def __init__(self, idx: int) -> None:
        self.idx = idx

    def run(self) -> None:
        print(f"Task {self.idx} is in progress")
        sleep(1)
        print(f"Task {self.idx} is finished")

def main():
    tasks = []
    for i in range(1, 4):
        tasks.append(Task(i))

    for task in tasks:
        task.run()

if __name__ == '__main__':
    main()
