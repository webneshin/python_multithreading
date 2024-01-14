from threading import Thread, Lock

"""
با مفاهیم مهمی مثل Race condition, Thread safe, Dead lock آشنا میشوید.
مشکل Race condition زمانی اتفاق میفتد که دو یا چند thread بخواهند به صورت همزمان به یک shared resouce دسترسی پیدا کنند.
در این حالت ممکن است ترد دوم در حین کار ترد اول به shared resource دسترسی پیدا کند و 
اطلاعات ناقصی که ترد اول در حال کار روی آنها بود را دریافت کند.
 برای حل این مشکل باید از کلاس Lock استفاده شود بصورتی که برنامه را با استفاده از متد acquire قفل کرده 
تا ترد دیگری نتواند به منابع دسترسی داشته باشد و بعد از اتمام کار با متد release برنامه را آزاد کند.
  در این حالت برنامه thread safe خواهد بود.
  مشکل dead lock زمانی اتفاق میفتد که به صورت اشتباه برنامه ای که با استفاده از متد acquire قفل شده بود
   را دوباره با متد acquire قفل کنیم. در این حالت برنامه block شده و نه پاسخی برگشت داده میشود و
نه برنامه تمام میشود. برای حل این مشکل پیشنهاد میشود که lock را به صورت یک context manager با متد with استفاده کنید.
"""

num = 0
lock = Lock()


def add():
    global num
    """
    در حالت کامنت شده اگر lock.release() فراموش شود برنامه قفل می شود.
    در حالت نوشده شده به صورت اتوماتیک release می شود. 
    """
    # lock.acquire()
    # for _ in range(10000000):
    #     num += 1
    # lock.release()
    with lock:
        for _ in range(10000000):
            num += 1
        a = 1 / 0


def subtract():
    global num
    # lock.acquire()
    # for _ in range(10000000):
    #     num -= 1
    # lock.release()
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
