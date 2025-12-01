from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_oled_128x64_v2 import BrickletOLED128x64V2
import time
from PIL import Image

ipcon = IPConnection()
ipcon.connect("localhost", 4223)
oled = BrickletOLED128x64V2("<YOUR_UID>", ipcon)
oled.clear_display()

def convert_rgb_to_bw(image_path):
    image = Image.open(image_path)
    w, h = image.size

    bw_values = []
    for y in range(h):
        for x in range(w):
            r, g, b = image.getpixel((x, y))

            if r == 255 and g == 255 and b == 255:
                bw_values.append(0)
            else:
                bw_values.append(1)

    return bw_values

pacman_half = convert_rgb_to_bw("bmp/pacman_half.bmp")
pacman_closed = convert_rgb_to_bw("bmp/pacman_closed.bmp")
pacman_open = convert_rgb_to_bw("bmp/pacman_open.bmp")

wait_time = 0.1
while True:
    oled.write_pixels(10, 10, 21, 22, pacman_closed)
    time.sleep(wait_time)
    oled.write_pixels(10, 10, 21, 22, pacman_half)
    time.sleep(wait_time)
    oled.write_pixels(10, 10, 21, 22, pacman_open)
    time.sleep(wait_time * 2)
    oled.write_pixels(10, 10, 21, 22, pacman_half)
    time.sleep(wait_time)