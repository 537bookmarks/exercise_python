
import time
import threading


def print_time(threadName,delay):
    count=0
    while count<5:
        time.sleep(delay)
        count=count+1
        print(f"{threadName}:{time.ctime()}")
        


thread1=threading.Thread(target=print_time,args=("Thread-1",2))
thread2=threading.Thread(target=print_time,args=("Thread-2",5))

thread1.start()
thread2.start()



while 1:
    pass


