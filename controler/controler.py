from model.model import Model
from view.view import View
import time

class Controler:
    def __init__(self, gpioStart, gpioRead):
        self.model = Model(gpioStart, gpioRead)
        self.view = View()
        self.view.set_controler(self)

    def cleanup(self):
        self.view.cleanup()

    def main(self):
        try:
            while True:
                potValue = self.model.update()
                self.view.update(potValue)
                time.sleep(5)
        except KeyboardInterrupt:
            self.cleanup()