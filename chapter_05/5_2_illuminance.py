from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_color_v2 import BrickletColorV2

ipcon = IPConnection()
ipcon.connect("localhost", 4223)
color_sensor = BrickletColorV2("<YOUR_UID>", ipcon)

illuminance = color_sensor.get_illuminance()

gain = 4
integration_time = 24
illuminance_lx = illuminance * 700 / gain / integration_time

print(f"Illuminance: {illuminance_lx} lx")