from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_rotary_encoder_v2 import BrickletRotaryEncoderV2
from tinkerforge.bricklet_rgb_led_v2 import BrickletRGBLEDV2

ipcon = IPConnection()
ipcon.connect("localhost", 4223)
knob = BrickletRotaryEncoderV2("<YOUR_UID>", ipcon)
led = BrickletRGBLEDV2("<YOUR_UID>", ipcon)

knob.reset()
brightness = 0
STEP = 10
led.set_rgb_value(brightness, brightness, brightness) 
last_count = 0

color = "white"
button_pressed_before = False

def set_led_color(color, brightness):
    if color == "white":
        led.set_rgb_value(brightness, brightness, brightness)
    if color == "yellow":
        led.set_rgb_value(brightness, brightness, 0)
    if color == "green":
        led.set_rgb_value(0, brightness, 0)

while True:
    new_count = knob.get_count(reset=False)
    button_pressed_after = knob.is_pressed()

    # If button changes from pressed to not pressed
    if button_pressed_before == True and button_pressed_after == False:
        if color == "white":
            color = "yellow"
        elif color == "yellow":
            color = "green"
        elif color == "green":
            color = "white"

        print(f"Color changed to: {color}")
        set_led_color(color, brightness)   

    button_pressed_before = button_pressed_after

    if new_count != last_count:
        diff = new_count - last_count
        last_count = new_count

        # Adjust brightness
        brightness += diff * STEP
        brightness = max(0, min(255, brightness))

        print(f"Brightness / Counter: {brightness} / {new_count}")
        set_led_color(color, brightness)