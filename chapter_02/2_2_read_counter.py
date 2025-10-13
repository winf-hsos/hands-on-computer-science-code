from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_rotary_encoder_v2 import BrickletRotaryEncoderV2

ipcon = IPConnection()
ipcon.connect("localhost", 4223)
knob = BrickletRotaryEncoderV2("<YOUR_UID>", ipcon)
count = knob.get_count(reset=False)

while True:
    count = knob.get_count(reset=False)
    print(count)