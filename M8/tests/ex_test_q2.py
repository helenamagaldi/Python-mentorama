import time
import threading
from threading import Thread

def proc1():
    time.sleep(5)
    print("fish")

def proc2():
    time.sleep(30)
    print("chips")

proc1()
proc2()

# __name__ == "__main__":
#    t1 = threading.Thread(target=proc1, arg=("more fish", "less fish"))
#    t2 = threading.Thread(target=proc2, arg=("more chips", "less chips"))

#    t1.start()
#    t2.start()

#    t1.join()
#    t2.join()

#    print(threading.activeCount())
