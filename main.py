from machine import UART, Pin
import time


uart0 = UART(0, baudrate=9600, tx=1, rx=3, bits=8, parity=None)
p = Pin(2, Pin.OUT)
p.value(1)

while 1:
    time.sleep(1)
    p.value((p.value() + 1) % 2)
    uart0.write(b'Hello\r\n')


print(1)