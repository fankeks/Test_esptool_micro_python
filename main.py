import machine
import time
import random
import _thread


exitstatus = [False for _ in range(2)]
def th(threadnum, arr1, arr2, start, stop):
    for i in range(start, stop):
        arr1[i] + arr2[i]
    exitstatus[threadnum] = True

print(machine.freq())
n = 3000
arr1 = [random.random() for _ in range(n)]
arr2 = [random.random() for _ in range(n)]

start = time.time_ns()
t1 = _thread.start_new_thread(th, (0, arr1, arr2, 0, n//2))
t2 = _thread.start_new_thread(th, (1, arr1, arr2, n//2, n))
while not(exitstatus[0] and exitstatus[0]):
    print(1)
print(time.time_ns() - start)


'''p0 = Pin(2, Pin.OUT)    # create output pin on GPIO0


def tim1(_):
    p0.value((p0.value()+1) % 2)
    print(0)


tim0 = Timer(0)
tim0.init(period=100, mode=Timer.PERIODIC, callback=tim1)


while 1:
    pass'''