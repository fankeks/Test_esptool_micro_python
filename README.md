# Libraris
Подготовка МК к работе:  
pip install esptool  
  
Прошивка микроконтроллера:  
pip install ampy  
pip install adafruit-ampy  
  
Для работы с COM портом:  
pip install pyserial  
# Commands  
Для очистки МК:  
python -m esptool --chip esp32 --port COM6 erase_flash  
  
Для конфигурации МК:  
python -m esptool --chip esp32 --port COM6 --baud 460800 write_flash -z 0x1000 ESP32_GENERIC-20240222-v1.22.2.bin  
  
Для запуска без записи:  
ampy --port COM6 run main.py  
  
Для прошивки:  
ampy --port COM6 put main.py  
# Links  
Гайд по esptool:  
https://micropython.org/download/ESP32_GENERIC/  
Гайд по работе с микропитоном:  
https://docs.micropython.org/en/latest/esp32/quickref.html#pins-and-gpio  
