from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_distance_ir_v2 import BrickletDistanceIRV2
from tinkerforge.bricklet_rgb_led_v2 import BrickletRGBLEDV2
import time

ipcon = IPConnection()
ipcon.connect("localhost", 4223)

ir = BrickletDistanceIRV2("<YOUR_UID>", ipcon)
led = BrickletRGBLEDV2("<YOUR_UID>", ipcon)

MESSAGE_LENGTH = 5 # Anzahl Bits pro Buchstabe
bits = ""
text = ""
last_distance = 0
receiving = False

# Dictionary mit 0–25 => A–Z und 26 => Leerzeichen
SYMBOLS = {}
SYMBOLS[0] = "A"
SYMBOLS[1] = "B"
SYMBOLS[2] = "C"
SYMBOLS[3] = "D"
SYMBOLS[4] = "E"
SYMBOLS[5] = "F"
SYMBOLS[6] = "G"
SYMBOLS[7] = "H"
SYMBOLS[8] = "I"
SYMBOLS[9] = "J"
SYMBOLS[10] = "K"
SYMBOLS[11] = "L"
SYMBOLS[12] = "M"
SYMBOLS[13] = "N"
SYMBOLS[14] = "O"
SYMBOLS[15] = "P"
SYMBOLS[16] = "Q"
SYMBOLS[17] = "R"
SYMBOLS[18] = "S"
SYMBOLS[19] = "T"
SYMBOLS[20] = "U"
SYMBOLS[21] = "V"
SYMBOLS[22] = "W"
SYMBOLS[23] = "X"
SYMBOLS[24] = "Y"
SYMBOLS[25] = "Z"
SYMBOLS[26] = " "

def decode_letter(bits):
    decimal = int(bits, 2)
    return SYMBOLS.get(decimal, "?")

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