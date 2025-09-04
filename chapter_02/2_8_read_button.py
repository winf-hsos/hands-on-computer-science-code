from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_rotary_encoder_v2 import BrickletRotaryEncoderV2
from tinkerforge.bricklet_rgb_led_v2 import BrickletRGBLEDV2

ipcon = IPConnection()
ipcon.connect('localhost', 4223)
knob = BrickletRotaryEncoderV2('WZd', ipcon) 
led = BrickletRGBLEDV2('ZG1', ipcon)

button_pressed_before = False
while True:
    button_pressed_after = knob.is_pressed()

    if button_pressed_before == True and button_pressed_after == False:
        print("Button was pressed and released")
    
    button_pressed_before = button_pressed_after