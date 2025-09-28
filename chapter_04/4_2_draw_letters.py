from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_oled_128x64_v2 import BrickletOLED128x64V2

ipcon = IPConnection()
ipcon.connect('localhost', 4223)
oled = BrickletOLED128x64V2('25zo', ipcon)
oled.clear_display()

def set_pixel(x, y, value):
    oled.write_pixels(x, y, x, y, [value])

# for y in range(0, 64):
#     for x in range(0, 128):
#         set_pixel(x, y, 1)


letter_a_bitmap = [
    0, 0, 1, 0, 0,
    0, 1, 0, 1, 0,
    1, 0, 0, 0, 1,
    1, 0, 0, 0, 1,
    1, 1, 1, 1, 1,
    1, 0, 0, 0, 1,
    1, 0, 0, 0, 1,
    0, 0, 0, 0, 0
]  

letter_s_bitmap = [
    0, 1, 1, 1, 0,
    1, 0, 0, 0, 1, 
    1, 0, 0, 0, 0,
    0, 1, 1, 1, 0,
    0, 0, 0, 0, 1, 
    1, 0, 0, 0, 1,
    0, 1, 1, 1, 0,
    0, 0, 0, 0, 0
]

oled.write_pixels(0, 10, 4, 17, letter_a_bitmap)
oled.write_pixels(6, 10, 10, 17, letter_s_bitmap)
oled.write_pixels(12, 10, 16, 17, letter_s_bitmap)

oled.write_line(0, 0, "Ass")