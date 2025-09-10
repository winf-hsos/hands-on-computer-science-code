from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_distance_ir_v2 import BrickletDistanceIRV2
from tinkerforge.bricklet_oled_128x64_v2 import BrickletOLED128x64V2
import random
import time

# Verbindung
ipcon = IPConnection()
ipcon.connect('localhost', 4223)

ir = BrickletDistanceIRV2('2a84', ipcon)
oled = BrickletOLED128x64V2('25zo', ipcon)

oled.clear_display()

# Klasse für Hindernisse
class Obstacle:
    def __init__(self, display):
        self.display = display
        self.width = 2
        self.height = random.randint(5, 20)
        self.y = random.randint(0, 64 - self.height)
        self.x = 122
        self.speed = random.randint(1, 5)
        self.counter = 0

    def draw(self, value):
        pixels = [value] * (self.width * self.height)
        self.display.write_pixels(self.x, self.y,
                                  self.x + self.width - 1,
                                  self.y + self.height - 1, pixels)

    def move(self):
        self.counter += 1
        if self.counter >= self.speed:
            self.counter = 0
            self.draw(0)
            self.x -= 1
            if self.x >= 0:
                self.draw(1)

    def is_off_screen(self):
        return self.x < 0

    def collides_with(self, player):
        return not (self.x + self.width < player.x or
                    self.x > player.x + player.width or
                    self.y + self.height < player.y or
                    self.y > player.y + player.height)

# Klasse für Spieler (Raumschiff nach rechts, spitze Nase)
class Player:
    def __init__(self, display):
        self.display = display
        self.x = 33
        self.y = 32
        # 7x7 Pfeil/Spaceship, Spitze zeigt nach rechts
        self.sprite = [
            [0,0,0,1,0,0,0],
            [0,0,1,1,1,0,0],
            [0,1,1,1,1,1,0],
            [1,1,1,1,1,1,1],
            [0,1,1,1,1,1,0],
            [0,0,1,1,1,0,0],
            [0,0,0,1,0,0,0]
        ]
        self.width = len(self.sprite[0])
        self.height = len(self.sprite)

    def _bbox(self):
        return (self.x, self.y,
                self.x + self.width - 1,
                self.y + self.height - 1)

    def draw(self, value):
        x1, y1, x2, y2 = self._bbox()
        if value == 0:
            pixels = [0] * (self.width * self.height)
        else:
            pixels = []
            for row in self.sprite:
                pixels.extend(row)
        self.display.write_pixels(x1, y1, x2, y2, pixels)

    def update_position(self, distance):
        # Distanz -> y (0..64-self.height) mappen, nicht aus dem Bild laufen
        if distance < 80:
            self.y = 64 - self.height
        elif distance > 260:
            self.y = 0
        else:
            self.y = int((260 - distance) / 180 * (64 - self.height))
        if self.y < 0: self.y = 0
        if self.y > 64 - self.height: self.y = 64 - self.height

    def explode(self):
        # 9x9 Comic-Explosion (wie gehabt)
        pattern = [
            [0,1,0,1,1,1,0,1,0],
            [1,1,1,0,1,0,1,1,1],
            [0,1,1,1,1,1,1,1,0],
            [1,0,1,1,0,1,1,0,1],
            [1,1,1,0,1,0,1,1,1],
            [1,0,1,1,1,1,1,0,1],
            [0,1,1,1,0,1,1,1,0],
            [1,1,0,1,1,1,0,1,1],
            [0,1,1,0,1,0,1,1,0]
        ]
        size = len(pattern)
        pixels = [v for row in pattern for v in row]

        ex = self.x - ((size - self.width) // 2)
        ey = self.y - ((size - self.height) // 2)
        if ex < 0: ex = 0
        if ey < 0: ey = 0
        if ex + size > 128: ex = 128 - size
        if ey + size > 64: ey = 64 - size

        self.display.write_pixels(ex, ey, ex + size - 1, ey + size - 1, pixels)
        time.sleep(1.0)
        self.display.clear_display()

# --- Spiel-Setup ---
player = Player(oled)
obstacles = []
counter = 0
next_obstacle_in = random.randint(30, 100)

start_time = time.time()
while True:
    # neue Hindernisse
    counter += 1
    if counter >= next_obstacle_in:
        counter = 0
        next_obstacle_in = random.randint(30, 100)
        obstacles.append(Obstacle(oled))

    # Spieler bewegen und zeichnen
    distance = ir.get_distance()
    player.draw(0)
    player.update_position(distance)
    player.draw(1)

    # Hindernisse bewegen + Kollision prüfen
    for o in obstacles[:]:
        o.move()
        if o.is_off_screen():
            obstacles.remove(o)
        elif o.collides_with(player):
            print("Kollision! Explosion!")
            player.explode()
            oled.clear_display()
            oled.write_line(3, 2, "G A M E   O V E R")
            end_time = time.time()
            oled.write_line(5, 2, f"YOUR SCORE: {int(end_time - start_time)}")
            exit()
