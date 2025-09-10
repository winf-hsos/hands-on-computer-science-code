from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_distance_ir_v2 import BrickletDistanceIRV2
from tinkerforge.bricklet_oled_128x64_v2 import BrickletOLED128x64V2

ipcon = IPConnection()
ipcon.connect('localhost', 4223)

ir = BrickletDistanceIRV2('2a84', ipcon)
oled = BrickletOLED128x64V2('25zo', ipcon)

oled.clear_display()

pos = 32
old_pos = -1
while True:
    distance = ir.get_distance()
    
    # The sensor measures between 40mm and 300mm, but the position should be 0 already at 280 mm and 60 already at 60 mm
    if distance < 80:
        pos = 60
    elif distance > 260:
        pos = 0
    else:
        pos = int((260 - distance) / 180 * 60)

    print(distance, pos)

    if pos != old_pos:
        old_pos = pos
        # Draw small rectangle in the middle of the display
        oled.clear_display()
        oled.write_pixels(33, pos, 36, pos + 3, [1] * 16)

