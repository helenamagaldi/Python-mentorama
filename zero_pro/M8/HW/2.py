import time
import threading
from threading import Thread


class Meal:
    def proc1(food):
        time.sleep(5)
        print(food, "fish")


    def proc2(food):
        time.sleep(30)
        print(food, "chips")


obj = Meal()
t1 = Thread(target=obj.proc1)
t2 = Thread(target=obj.proc2)

t1.start()
t2.start()

print(threading.activeCount())



