from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_oled_128x64_v2 import BrickletOLED128x64V2

ipcon = IPConnection()
ipcon.connect("localhost", 4223)
oled = BrickletOLED128x64V2("<YOUR_UID>", ipcon)
oled.clear_display()

oled.write_pixels(0, 0, 0, 0, [1])
input("Press Enter to turn off the pixel...")
oled.write_pixels(0, 0, 0, 0, [0])