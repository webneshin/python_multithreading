import time
from threading import Thread
from time import sleep


def slow(name: str) -> None:
    print(f"starting {name}")
    sleep(3)
    print(f"finisging {name}")


class SlowThread(Thread):
    def __init__(self, name: str) -> None:
        super().__init__()
        self.name = name

    def run(self) -> None:
        slow(self.name)


start = time.perf_counter()

t1 = SlowThread('first')
t2 = SlowThread('second')

t1.start()
t2.start()

t1.join()
t2.join()

end = time.perf_counter()
print(f"multi thread run in '{end - start}' seconds")
