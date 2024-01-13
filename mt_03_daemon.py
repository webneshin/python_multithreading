import sys
import time
from threading import Thread
from time import sleep

"""
به صورت پیشفرض مقدار daemon برابر False است یعنی برنامه مجبور است تا تمام شدن کار thread صبر کند.

اگر از t1.join() و t2.join() استفاده شود daemon تاثیری ندارد. زیرا منتظر می مانیم تا آن thread انجام شود

می توانیم برای ست کردن daemon قبل از start از t1.setDaemon() برای ست کردنش استفاده کنیم.

با t1.daemon یا t1.isDaemon() می شود .ضعیتش را دید
"""


def slow(name: str) -> None:
    print(f"starting {name}")
    sleep(3)
    print(f"finisging {name}")


start = time.perf_counter()

t1 = Thread(target=slow, args=("first",), daemon=True)  # daemon رو False کن تا تغییر را ببینی
t2 = Thread(target=slow, args=("seconds",), daemon=True)  # daemon رو False کن تا تغییر را ببینی
t1.start()
t2.start()


end = time.perf_counter()
print(f"multi thread run in '{end - start}' seconds")
sys.exit()
