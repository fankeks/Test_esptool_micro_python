#import machine
import time
import random
#import _thread
from threading import Thread


exitstatus = [False for _ in range(2)]
def th(threadnum, arr1, arr2, start, stop):
    for i in range(start, stop):
        arr1[i] + arr2[i]
    exitstatus[threadnum] = True

#print(machine.freq())
n = 30000000
arr1 = [random.random() for _ in range(n)]
arr2 = [random.random() for _ in range(n)]

t1 = Thread(target=th, args=(0, arr1, arr2, 0, n))
t2 = Thread(target=th, args=(1, arr1, arr2, 0, n))
start = time.time_ns()
t1.start()
t2.start()
'''t1 = _thread.start_new_thread(th, (0, arr1, arr2, 0, n))
t2 = _thread.start_new_thread(th, (1, arr1, arr2, 0, n))
while not(exitstatus[0] and exitstatus[0]):
    pass'''
t1.join()
t2.join()
print(time.time_ns() - start)


'''p0 = Pin(2, Pin.OUT)    # create output pin on GPIO0


def tim1(_):
    p0.value((p0.value()+1) % 2)
    print(0)


tim0 = Timer(0)
tim0.init(period=100, mode=Timer.PERIODIC, callback=tim1)


while 1:
    pass'''