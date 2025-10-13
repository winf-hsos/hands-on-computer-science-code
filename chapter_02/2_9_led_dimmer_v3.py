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

button_pressed_before = False

# 1. Main loop to keep program running
while True:
    new_count = knob.get_count(reset=False)
    button_pressed_after = knob.is_pressed()

    # 2. Logic for color change on button release
    if button_pressed_before == True and button_pressed_after == False:
        if color == "white":
            color = "yellow"
        elif color == "yellow":
            color = "green"
        elif color == "green":
            color = "white"

        # Update LED to reflect new color
        if color == "white":
            led.set_rgb_value(brightness, brightness, brightness)
        if color == "yellow":
            led.set_rgb_value(brightness, brightness, 0)
        if color == "green":
            led.set_rgb_value(0, brightness, 0)

    button_pressed_before = button_pressed_after

    # 3. Logic for brightness adjustment
    if new_count != last_count:
        diff = new_count - last_count
        last_count = new_count

        # Adjust brightness
        brightness += diff * STEP
        brightness = max(0, min(255, brightness))

        # Update LED to reflect new color
        if color == "white":
            led.set_rgb_value(brightness, brightness, brightness)
        if color == "yellow":
            led.set_rgb_value(brightness, brightness, 0)
        if color == "green":
            led.set_rgb_value(0, brightness, 0)

        print(f"Brightness / Counter: {brightness} / {new_count}")