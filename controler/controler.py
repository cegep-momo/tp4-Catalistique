from model.model import Model
from view.view import View
import time

class Controler:
    def __init__(self, gpioStart, gpioRead):
        self.model = Model(gpioStart, gpioRead, self)
        self.view = View()
        self.view.setControler(self)
        self.model.startThreadStart()
        self.model.startThreadRead()

    def cleanup(self):
        self.view.cleanup()
        self.model.stoppingProgram = True

    def updateView(self):
        self.view.update(self.model.update())

    def main(self):
        try:
            self.view.readingsOffScreen()
            while True:
                while self.model.started:
                    self.view.update(self.model.update())
                    self.model.saveReading()
                    time.sleep(5)
                time.sleep(0.1)
        except KeyboardInterrupt:
            self.cleanup()