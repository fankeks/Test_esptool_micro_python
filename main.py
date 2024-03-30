from machine import ADC, Pin


adc = ADC(Pin(12))

while 1:
    val = adc.read()
    print(val)