from model.model import Model
from view.view import View
import time

class Controler:
    def __init__(self, gpioStart, gpioRead):
        """
        Initializes the Controler class by setting up the model and view components.

        Args:
            gpioStart (int): GPIO pin number for the start button.
            gpioRead (int): GPIO pin number for the read button.
        """
        self.model = Model(gpioStart, gpioRead, self)
        self.view = View()
        self.view.setControler(self)
        self.model.startThreadStart()
        self.model.startThreadRead()

    def cleanup(self):
        """
        Cleans up resources by stopping the program and clearing the LCD display.
        """
        self.view.cleanup()
        self.model.stoppingProgram = True

    def updateView(self):
        """
        Updates the view with the latest potentiometer value from the model.
        """
        self.view.update(self.model.update())

    def main(self):
        """
        Main loop of the controller, managing the interaction between the model and view.
        Handles the start and stop of the system and updates the view periodically.
        """
        try:
            self.view.readingsOffScreen()
            while True:
                while self.model.started and not self.model.platine.isReading:
                    self.model.platine.isReading = True
                    self.view.update(self.model.update())
                    self.model.saveReading()
                    self.model.platine.isReading = False
                    time.sleep(1)
                time.sleep(0.1)
        except KeyboardInterrupt:
            self.cleanup()