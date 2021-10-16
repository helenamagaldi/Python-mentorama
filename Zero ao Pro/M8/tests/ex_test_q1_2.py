import threading
from threading import Thread
import time 


class Test1:
    def test_thread(self):
        print("First Process")


obj = Test1()
t1 = Thread(target=obj.test_thread)
t1.start()