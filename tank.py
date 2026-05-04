import random

class TankSystem:
    def __init__(self):
        self.water_level = 70
        self.pump_on = False

    def update(self):
        self.water_level -= random.uniform(0.5, 1.5)

    def control(self):
        if self.water_level < 20:
            print("WARNING: Critical low level!")

        if self.water_level >= 70 and self.pump_on:
            self.pump_on = False
            print("Pump OFF")

        elif self.water_level < 30 and not self.pump_on:
            self.pump_on = True
            print("Pump ON")

        if self.pump_on:
            self.water_level += 5

    def display(self):
        print(f"Water Level: {self.water_level:.1f}% | Pump: {self.pump_on}")
