import random

class Environment:
    def __init__(self):
        self.temp = 28
        self.rh = 65
        self.lux = 50000
        self.screen_closed = False

    def update(self):
        self.temp += random.uniform(-0.4, 0.6)
        self.rh += random.uniform(-1, 1)
        self.lux += random.uniform(-5000, 5000)

    def control(self):
        if self.lux > 70000:
            self.screen_closed = True
            self.temp -= 1.0
        else:
            self.screen_closed = False

        if self.temp > 30:
            print("Fan-Pad ON → Cooling activated")
            self.temp -= 1.5

        if self.rh < 60:
            print("Fogger ON")
            self.rh += 5

    def display(self):
        print(f"Temp: {self.temp:.2f} °C | RH: {self.rh:.2f}% | Lux: {self.lux:.0f}")
