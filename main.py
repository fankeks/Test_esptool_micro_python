import machine
import time
import random

print(machine.freq())
n = 3000
arr1 = [random.random() for _ in range(n)]
arr2 = [random.random() for _ in range(n)]

start = time.time_ns()
for i in range(n):
    arr1[i] + arr2[i]
    #print(arr3[i])
print(time.time_ns() - start)


'''p0 = Pin(2, Pin.OUT)    # create output pin on GPIO0


def tim1(_):
    p0.value((p0.value()+1) % 2)
    print(0)


tim0 = Timer(0)
tim0.init(period=100, mode=Timer.PERIODIC, callback=tim1)


while 1:
    pass'''