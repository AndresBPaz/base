# enciende el led en la placa
import time
from machine import Pin

led = Pin(13, Pin.OUT)

while True:
    led.value(1)
    time.sleep(1)