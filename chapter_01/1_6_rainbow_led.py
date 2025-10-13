import time
from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_rgb_led_v2 import BrickletRGBLEDV2

ipcon = IPConnection()
ipcon.connect("localhost", 4223)
led = BrickletRGBLEDV2("<YOUR_UID>", ipcon)

# Turn LED off initially
led.set_rgb_value(0, 0, 0)

rainbow_duration = 5
pause_duration = rainbow_duration / 1536

while True:

    # phase 1
    for green in range(256):
        led.set_rgb_value(255, green, 0)
        time.sleep(pause_duration)

    # phase 2
    for red in range(255, -1, -1):
        led.set_rgb_value(red, 255, 0)
        time.sleep(pause_duration)

    # phase 3
    for blue in range(256):
        led.set_rgb_value(0, 255, blue)
        time.sleep(pause_duration)

    # phase 4
    for green in range(255, -1, -1):
        led.set_rgb_value(0, green, 255)
        time.sleep(pause_duration)

    # phase 5
    for red in range(256):
        led.set_rgb_value(red, 0, 255)
        time.sleep(pause_duration)

    # phase 6
    for blue in range(255, -1, -1):
        led.set_rgb_value(255, 0, blue)
        time.sleep(pause_duration)