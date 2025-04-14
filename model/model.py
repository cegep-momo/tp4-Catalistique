from .platine import Platine
from .mesure import Mesure
import threading, time, datetime, json

class Model:
    def __init__(self, gpioStart, gpioRead, controler):
        """
        Initializes the Model class with GPIO pins and a controller.

        Args:
            gpioStart (int): GPIO pin number for the start button.
            gpioRead (int): GPIO pin number for the read button.
            controler: The controller instance to link with the model.
        """
        self.controler = controler
        self.platine = Platine(gpioStart, gpioRead)
        self.started = False
        self.stoppingProgram = False

    def startThreadStart(self):
        """
        Starts a thread to monitor the start button.
        """
        self.threadStart = threading.Thread(target=self.start, daemon=True)
        self.threadStart.start()

    def startThreadRead(self):
        """
        Starts a thread to monitor the read button.
        """
        self.threadRead = threading.Thread(target=self.read, daemon=True)
        self.threadRead.start()

    def start(self):
        """
        Monitors the start button and toggles the system state.
        """
        while not self.stoppingProgram:
            if self.started:
                self.update()
                if self.platine.ifStartPressed():
                    self.started = False
                    self.controler.view.readingsOffScreen()
            else:
                if self.platine.ifStartPressed():
                    self.started = True
            time.sleep(0.1)
    
    def read(self):
        """
        Monitors the read button to update the view and save the current reading.
        """
        while not self.stoppingProgram:
            if self.platine.ifReadPressed() and not self.platine.isReading:
                self.platine.isReading = True
                self.controler.updateView()
                self.saveReading()
                self.platine.isReading = False
            time.sleep(0.1)

    def update(self):
        """
        Reads the potentiometer value from the platine.

        Returns:
            float: The current potentiometer value.
        """
        self.potValue = self.platine.readPotentiometer()

        return self.potValue
    
    def saveReading(self):
        """
        Saves the current potentiometer value as a measurement.
        """
        measurement = Mesure(datetime.datetime.now(), [self.potValue])
        measurement.saveReading()