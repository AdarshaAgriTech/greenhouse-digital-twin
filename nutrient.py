import random

class NutrientSystem:
    def __init__(self):
        self.ec = 1.8
        self.ph = 6.2

    def update(self):
        self.ec += random.uniform(-0.05, 0.02)
        self.ph += random.uniform(-0.05, 0.05)

    def control(self):
        if self.ec < 1.5:
            print("EC LOW → Adding nutrient stock")
            self.ec += 0.3

        elif self.ec > 2.5:
            print("EC HIGH → Adding water")
            self.ec -= 0.3

        if self.ph > 6.5:
            print("pH HIGH → Adding acid")
            self.ph -= 0.2

        elif self.ph < 5.5:
            print("pH LOW → Adding base")
            self.ph += 0.2

    def display(self):
        print(f"EC: {self.ec:.2f} dS/m | pH: {self.ph:.2f}")
