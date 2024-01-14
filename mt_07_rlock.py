from threading import Thread, Lock, RLock

"""
در زمانهایی که برنامه ما نیاز دارد که یک متد را چند بار صدا بزند یا برنامه به شکل بازگشتی باشد
 استفاده از lock به عنوان context manager فایده نخواهد داشت و برنامه block خواهد شد.
  در این حالت میتوانید از Rlock به جای lock استفاده کنید.
   با استفاده از Rlock میتوانید چندین بار acquire کرده بدون اینکه برنامه block شود.
"""

num = 0
# lock = Lock()
lock = RLock()


def add():
    global num
    with lock:
        subtract()
        for _ in range(10000000):
            num += 1


def subtract():
    global num
    with lock:
        for _ in range(10000000):
            num -= 1


t1 = Thread(target=add)
t2 = Thread(target=subtract)

t1.start()
t2.start()

t1.join()
t2.join()

print(num)
print("Done!")
