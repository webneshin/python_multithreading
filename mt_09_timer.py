from threading import Timer


def slow():
    print("Hi Webneshin!!")


t = Timer(5,slow)

t.start()