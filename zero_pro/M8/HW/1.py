import threading
from threading import Thread

class Test1:
    def test_thread(self):
        print("First Process")


obj = Test1()
t1 = Thread(target=obj.test_thread)
t1.start()

print(threading.activeCount())

print(threading.currentThread())

print(threading.get_ident())

print(threading.enumerate())

print(threading.activeCount())


        





