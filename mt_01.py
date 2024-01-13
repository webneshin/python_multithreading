import time
from threading import Thread
from time import sleep


def slow(name: str) -> None:
    print(f"starting {name}")
    sleep(3)
    print(f"finisging {name}")


# start multithreading
print(s := "start single threading", "*" * (120 - len(s)))

start = time.perf_counter()

slow("first")
slow("second")

end = time.perf_counter()
print(f"single thread run in '{end - start}' seconds")

# start multithreading
print(s := "start multit hreading", "*" * (120 - len(s)))

start = time.perf_counter()

t1 = Thread(target=slow, args=("first",))
t2 = Thread(target=slow, args=("seconds",))
t1.start()
t2.start()
t1.join()
t2.join()

end = time.perf_counter()
print(f"multi thread run in '{end - start}' seconds")
