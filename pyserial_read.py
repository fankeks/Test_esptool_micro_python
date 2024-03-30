import serial


with serial.Serial('COM6', 9600) as mcu:
    print('Start')
    while 1:
        val = str(mcu.readline().decode())
        print(val)

