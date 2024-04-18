# Багатопоточність

from time import sleep
from threading import Thread


class Task(Thread):
    def __init__(
            self, group=None, target=None, name=None,
            args=(), kwargs=None, *, daemon=None
    ):
        super().__init__(group=group, target=target, name=name, daemon=daemon)
        self.args = args
        self.kwargs = kwargs

    def run(self) -> None:
        print(f"Task {self.args[0]} is in progress")
        sleep(1)
        print(f"Task {self.args[0]} is finished")


if __name__ == '__main__':
    threads = []

    for i in range(1, 4):
        thread = Task(args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    
    print("All threads are finished")
