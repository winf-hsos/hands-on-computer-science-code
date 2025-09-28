from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_distance_ir_v2 import BrickletDistanceIRV2
from tinkerforge.bricklet_rgb_led_v2 import BrickletRGBLEDV2

ipcon = IPConnection()
ipcon.connect('localhost', 4223)
ir = BrickletDistanceIRV2('2a7S', ipcon) 

led = BrickletRGBLEDV2('ZEL', ipcon)
led.set_rgb_value(0, 0, 0)  # Set initial color to off

last_distance = 0
while True:
    distance = ir.get_distance()
    if last_distance != distance:
        last_distance = distance

        # Map distance to LED brightness (0-255)
        brightness = int((distance - 40) / (300 - 40) * 255)

        led.set_rgb_value(brightness, brightness, brightness)  # Set LED color