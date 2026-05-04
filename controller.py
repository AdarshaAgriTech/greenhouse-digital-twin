from environment import Environment
from nutrient import NutrientSystem
from tank import TankSystem
import time

class GreenhouseController:
    def __init__(self):
        self.env = Environment()
        self.nutrient = NutrientSystem()
        self.tank = TankSystem()

    def update(self):
        self.env.update()
        self.nutrient.update()
        self.tank.update()

    def control(self):
        self.env.control()
        self.nutrient.control()
        self.tank.control()

        # interaction
        if self.tank.pump_on:
            self.nutrient.ec -= 0.05

        if self.env.temp > 30:
            print("High Temp → Increased water consumption")
            self.tank.water_level -= 1

    def display(self):
        print("\n====== GREENHOUSE STATUS ======")
        self.env.display()
        self.nutrient.display()
        self.tank.display()


if __name__ == "__main__":
    system = GreenhouseController()

    for i in range(5):
        system.update()
        system.control()
        system.display()
        print("----------------")
        time.sleep(1)
