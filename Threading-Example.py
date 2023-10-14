import threading
import time


def old():
    x=0
    while(x<=10):
        print("x",x)
        time.sleep(0.08)
        x=x+1


def new():
    y=0
    while(y<=20):
        print("y",y)
        time.sleep(0.08)
        y=y+1
        
t1=threading.Thread(target=new)
t2=threading.Thread(target=old)
t1.start()
t2.start()
t1.join()
t2.join()

print("Main Thread Here!!")