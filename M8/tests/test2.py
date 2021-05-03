import threading
from threading import Thread
import time 


class MyThread:
    def showNumbers(self):
        i = 0
        print(threading.current_thread().getName())
        time.sleep(1)
        while(i<=10):
            print(i)
            i+=1

obj = MyThread()
t1 = Thread(target=obj.showNumbers)
t1.start()

t2 = Thread(target=obj.showNumbers)
t2.start()

t3 = Thread(target=obj.showNumbers)
t3.start()