from concurrent.futures.thread import ThreadPoolExecutor
from time import sleep


def slow(name: str) -> None:
    print(s := f"starting {name}", "*" * (120 - len(s)))
    sleep(3)
    print(f"finisging {name}")


with ThreadPoolExecutor(max_workers=7) as executor:
    names = ["1th", "2th", "3th", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th", "13th", "14th"]
    executor.map(slow,names)

print("Done!")
