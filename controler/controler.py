from model.model import Model
from view.view import View
import time

class Controler:
    def __init__(self, gpioStart, gpioRead):
        self.model = Model(gpioStart, gpioRead)
        self.view = View()
        self.view.set_controler(self)
        self.model.start_thread_start()
        self.model.start_thread_read()

    def cleanup(self):
        self.view.cleanup()
        

    def main(self):
        try:
            while True:
                while self.model.started:
                    self.view.update(self.model.update())
                    time.sleep(5)
                time.sleep(0.1)
        except KeyboardInterrupt:
            self.cleanup()