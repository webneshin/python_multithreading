from threading import Event, Thread


"""
آبجکت های Event زمانی کاربرد دارند که بخواهید چند thread با هم ارتباط داشته و از وضعیت همدیگر با خبر باشند.
در این آبجکت های با استفاده از متد set تردها میتوانند آمادگی خود را برای انجام کار اعلام کنند
و با متد wait اعلام کنند که منتظر پاسخ از سمت بقیه تردها هستند.
در این حالت تردهای دیگر میتوانند دوباره با متد set به ترد قبلی متصل شده با هم کار کنند
"""


def first(f, s):
    print('first is ready ...')
    f.set()
    s.wait()
    print('first is working ...')
    f.clear()


def second(f, s):
    print('second is ready ...')
    s.set()
    f.wait()
    print('second is working ...')
    s.clear()


f = Event()
s = Event()

t1 = Thread(target=first, args=(f, s))
t2 = Thread(target=second, args=(f, s))

t1.start()
t2.start()
