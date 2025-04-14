from .platine import Platine

class Model:
    def __init__(self, gpioStart, gpioRead):
        self.platine = Platine(gpioStart, gpioRead)

    def update(self):
        self.potValue = self.platine.read_potentiometer()

        return self.potValue