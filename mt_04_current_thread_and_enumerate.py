import threading
import time
from threading import Thread
from time import sleep

"""
متد current_thread تردی که در حال حاضر فعال است را برمیگرداند و
 متد enumerate تمامی تردهایی که فعال هستند را برمیگرداند.
  دقت کنید که متد enumerate تردهایی که هنوز شروع نشده اند یا تردهایی که تمام شده اند را نشان نمیدهد


"""


def slow(name: str) -> None:
    print(s := f"starting {name}", "*" * (120 - len(s)))
    print("current_thread:", threading.current_thread())
    print("enumerate:", threading.enumerate())
    print("active_count:", threading.active_count())
    sleep(3)
    print(f"finisging {name}")


t1 = Thread(target=slow, args=("first",))
t2 = Thread(target=slow, args=("seconds",))
t1.start()
t2.start()
t1.join()
t2.join()
print(s := f"finished all threads", "*" * (120 - len(s)))
print("current_thread:", threading.current_thread())
print("enumerate:", threading.enumerate())
print("active_count:", threading.active_count())
print("Done!")
