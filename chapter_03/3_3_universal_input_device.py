from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_distance_ir_v2 import BrickletDistanceIRV2
import time

ipcon = IPConnection()
ipcon.connect("localhost", 4223)
ir = BrickletDistanceIRV2("<YOUR_UID>", ipcon)

last_distance = 0
receiving = False
while True:
    distance = ir.get_distance()
    if last_distance != distance:

        # Wait 100 ms and measure again
        time.sleep(0.1) 
        distance = ir.get_distance()
        
        if receiving:
            if distance > 170 and distance < 300:
                print(f"1 at {distance} mm")
                receiving = False
            elif distance <= 170:
                print(f"0 at {distance} mm")
                receiving = False
        else:
            if distance >= 300:
                receiving = True
                print(f"Ready to receive next code")

        last_distance = distance