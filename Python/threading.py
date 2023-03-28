from time import sleep
from threading import *

# Multi-threading - same code get divided into multiple pieces that runs simultaneously

class Hello(Thread):
    def run(self):
        for i in range(10):
            print('Hello')
            sleep(0.5)
        
class Hi(Thread):
    def run(self):
        for i in range(10):
            print('Hi')
            sleep(0.5)


t1 = Hello()
t1.start()                  # new thread created leaving main thread and run method get exicuted

sleep(0.5)

t2 = Hi()                   # new thread created leaving main thread and run method get exicuted
t2.start()

t1.join()                   #|
t2.join()                   #| Both the thread gets rejoined in main thread

print('Bye')                # Exicuted by main tread