from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_distance_ir_v2 import BrickletDistanceIRV2
from tinkerforge.bricklet_rgb_led_v2 import BrickletRGBLEDV2
import time

ipcon = IPConnection()
ipcon.connect("localhost", 4223)

ir = BrickletDistanceIRV2("<YOUR_UID>", ipcon)
led = BrickletRGBLEDV2("<YOUR_UID>", ipcon)

MESSAGE_LENGTH = 7 # Anzahl Bits pro Buchstabe
bits = ""
text = ""
last_distance = 0
receiving = False

def decode_letter(bits):
    # Füge links eine 0 hinzu, damit es 8 Bits sind
    bits = "0" + bits

    # Konvertiere Binärstring in Dezimalzahl und dann in ASCII-Zeichen
    decimal = int(bits, 2)
    return chr(decimal)

while True:
    distance = ir.get_distance()
    if last_distance != distance:

        time.sleep(0.1) 
        distance = ir.get_distance()
        
        if receiving:
            if distance > 170 and distance < 300:
                print("1")
                bits += "1"
                receiving = False
            elif distance <= 170:
                print("0")
                bits += "0"
                receiving = False

            if len(bits) == MESSAGE_LENGTH: 
                print(f"Bits: {bits}")
                letter = decode_letter(bits)

                print(f"Letter: {letter}")
                text += letter
                
                print(f"Text: {text}")
                bits = ""
        else:
            if distance >= 300:
                receiving = True
            
        last_distance = distance