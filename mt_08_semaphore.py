from threading import Thread, Semaphore, current_thread, enumerate, BoundedSemaphore
from time import sleep

"""
 گزینه semaphore وظیفه ای مشابه lock دارد اما برای زمان هایی استفاده میشود که نیاز داشته باشید
در تعداد threadهایی که به shared resource متصل میشوند کنترل داشته باشید.
در کلاس semaphore یک counter یا شمارشگر وجود دارد که تعداد threadهای متصل را کنترل میکند.
هر بار که یک thread از متد acquire استفاده میکند یک عدد از این counter کم شده
و هربار که از متد release استفاده میشود به این عدد اضافه میشود.
زمانی که این عدد به صفر برسد هیچ thread دیگری پذیرفته نیست و باید منتظر بمانند.
همچنین در این ویدیو با کلاس BoundedSemaphore هم آشنا میشوید.
در کلاس semaphore اگر شما بیشتر از تعداد acquire از release استفاده کنید تعداد counter منفی شده
و باعث میشود در مرحله بعد تعداد threadهای بیشتری کار کنند.
برای حل این مشکل میتوانید از کلاس BoundedSemaphor استفاده کنید
که در صورت منفی شدن counter پیغام خطای ValueError خواهد داد.
"""

num = 0

# lock = Semaphore(value=2)
lock = BoundedSemaphore(value=2)


def add():
    global num
    lock.acquire()
    sleep(2)
    num += 1
    lock.release()
    lock.release()
    lock.release()
    lock.release()
    lock.release()
    lock.release()
    lock.release()
    lock.release()
    lock.release()


t1 = Thread(target=add)
t2 = Thread(target=add)
t3 = Thread(target=add)
t4 = Thread(target=add)
t5 = Thread(target=add)
t6 = Thread(target=add)
t7 = Thread(target=add)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()

stop = False
while True:
    print(enumerate())
    print(num)
    sleep(1)
    if stop:
        break
    if num == 7:
        stop = True

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
