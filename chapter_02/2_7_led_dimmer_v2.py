from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_rotary_encoder_v2 import BrickletRotaryEncoderV2
from tinkerforge.bricklet_rgb_led_v2 import BrickletRGBLEDV2

ipcon = IPConnection()
ipcon.connect("localhost", 4223)
knob = BrickletRotaryEncoderV2("<YOUR_UID>", ipcon)
led = BrickletRGBLEDV2("<YOUR_UID>", ipcon)

knob.reset()
brightness = 0
led.set_rgb_value(brightness, brightness, brightness) 
STEP = 10

last_count = 0
while True:
    new_count = knob.get_count(reset=False)

    if new_count != last_count:
        diff = new_count - last_count
        last_count = new_count

        # Adjust brightness
        brightness += diff * STEP
        brightness = max(0, min(255, brightness))

        # Setze RGB-Werte auf den Zählerwert
        led.set_rgb_value(brightness, brightness, brightness)

        print(f"Brightness / Counter: {brightness} / {new_count}")