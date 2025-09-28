import time
from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_rgb_led_v2 import BrickletRGBLEDV2

ipcon = IPConnection()
ipcon.connect("localhost", 4223)
led = BrickletRGBLEDV2("ZEP", ipcon)

# Turn LED off initially
led.set_rgb_value(0, 0, 0)

while True:

    # Increase red step by step
    for r in range(256):
        led.set_rgb_value(r, 0, 0)
        time.sleep(0.001)

    # Stay at full brightness for a bit
    time.sleep(0.25)

    # Decrease red step by step
    for r in range(255, -1, -1):
        led.set_rgb_value(r, 0, 0)
        time.sleep(0.001)

    # Stay at full dark for a bit
    time.sleep(0.25)