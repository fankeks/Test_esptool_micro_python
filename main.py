from machine import Pin
from machine import Timer


p0 = Pin(2, Pin.OUT)    # create output pin on GPIO0


def tim1(_):
    p0.value((p0.value()+1) % 2)
    print(0)


tim0 = Timer(0)
tim0.init(period=100, mode=Timer.PERIODIC, callback=tim1)


while 1:
    pass