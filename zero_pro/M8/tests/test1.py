from threading import Thread
import time


def func1():
    for x in range(1,11):
        print("First Process", x)
        time.sleep(2)
        x += 1

def func2():
    for x in range(1,11):
        print("Second Process", x)
        time.sleep(1)
        x += 1

t1 = Thread(target=func1).start()
t2 = Thread(target=func2).start()
