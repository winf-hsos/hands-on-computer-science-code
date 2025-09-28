from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_oled_128x64_v2 import BrickletOLED128x64V2

ipcon = IPConnection()
ipcon.connect('localhost', 4223)
oled = BrickletOLED128x64V2('25zo', ipcon)
oled.clear_display()

def draw_house(oled, x, y, scale=1):
    width = round(15 * scale)
    height = round(15 * scale)
    
    # Wände
    oled.write_pixels(x, y + height // 2, x + width - 1, y + height - 1, [1] * (width * (height // 2)))
    
    # Dach
    roof_height = height // 2
    for i in range(roof_height):
        oled.write_pixels(x + i, y + roof_height - i - 1, x + width - i - 1, y + roof_height - i - 1, [1] * (width - 2 * i))
    
    # Tür
    door_width = max(1, width // 5)
    door_height = max(1, height // 4)
    door_x = x + (width - door_width) // 2
    door_y = y + height - door_height
    oled.write_pixels(door_x, door_y, door_x + door_width - 1, door_y + door_height - 1, [0] * (door_width * door_height))

    # Fenster
    window_size = max(1, width // 5)
    window_x = x + width // 4 - window_size // 2
    window_y = y + height // 2 - window_size // 2
    oled.write_pixels(window_x, window_y, window_x + window_size - 1, window_y + window_size - 1, [0] * (window_size * window_size))
    window_x = x + 3 * width // 4 - window_size // 2
    oled.write_pixels(window_x, window_y, window_x + window_size - 1, window_y + window_size - 1, [0] * (window_size * window_size))

draw_house(oled, 5, 5, scale=1)
input("Press Enter to continue...")
oled.clear_display()
draw_house(oled, 5, 5, scale=1.5)
input("Press Enter to continue...")
oled.clear_display()
draw_house(oled, 5, 5, scale=2)
input("Press Enter to continue...")
oled.clear_display()
draw_house(oled, 5, 5, scale=3)
input("Press Enter to finish...")
oled.clear_display()
draw_house(oled, 5, 5, scale=.7)