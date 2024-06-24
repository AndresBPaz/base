import time
from machine import Pin

# Define the LED pin number
led_pin = 25  # Replace with the actual GPIO pin number you connected the LED to

# Create a Pin object for the LED
led = Pin(led_pin, Pin.OUT)

# Blink the LED (on for 1 second, off for 1 second)
while True:
    led.value(1)  # Set the LED pin to HIGH (turn on)
    time.sleep(1)
    led.value(0)  # Set the LED pin to LOW (turn off)
    time.sleep(1)
