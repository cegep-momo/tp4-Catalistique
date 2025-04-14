from .platine import Platine
from .mesure import Mesure
import threading, time, datetime, json

class Model:
    def __init__(self, gpioStart, gpioRead, controler):
        self.controler = controler
        self.platine = Platine(gpioStart, gpioRead)
        self.started = False
        self.stoppingProgram = False

    def startThreadStart(self):
        self.threadStart = threading.Thread(target=self.start, daemon=True)
        self.threadStart.start()

    def startThreadRead(self):
        self.threadRead = threading.Thread(target=self.read, daemon=True)
        self.threadRead.start()

    def start(self):
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
        while not self.stoppingProgram:
            if self.platine.ifReadPressed():
                self.controler.updateView()
                self.saveReading()
            time.sleep(0.1)

    def update(self):
        self.potValue = self.platine.readPotentiometer()

        return self.potValue
    
    def saveReading(self):
        measurement = Mesure(datetime.datetime.now(), [self.potValue])
        measurement.saveReading()