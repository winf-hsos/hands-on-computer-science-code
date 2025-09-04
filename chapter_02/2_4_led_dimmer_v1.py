from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_rotary_encoder_v2 import BrickletRotaryEncoderV2
from tinkerforge.bricklet_rgb_led_v2 import BrickletRGBLEDV2

ipcon = IPConnection()
ipcon.connect('localhost', 4223)
knob = BrickletRotaryEncoderV2('WZd', ipcon) 
led = BrickletRGBLEDV2('ZG1', ipcon)

knob.reset()
last_count = 0
print(last_count)

while True:
    new_count = knob.get_count(reset=False)

    if new_count != last_count:
        last_count = new_count
        print(last_count)

        # Setze RGB-Werte auf den Zählerwert
        led.set_rgb_value(last_count, last_count, last_count)