from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_oled_128x64_v2 import BrickletOLED128x64V2

ipcon = IPConnection()
ipcon.connect("localhost", 4223)
oled = BrickletOLED128x64V2("<YOUR_UID>", ipcon)
oled.clear_display()

cross_bitmap = [0, 1, 0, 1, 1, 1, 0, 1, 0]
for y in range(0, 64, 4):
    for x in range(0, 128, 4):
        oled.write_pixels(x, y, x + 2, y + 2, cross_bitmap)