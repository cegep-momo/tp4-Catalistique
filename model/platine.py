from gpiozero import MCP3008, Button

class Platine:
    def __init__(self, gpioStart, gpioRead):
        self.gpioPot = MCP3008(channel=0)
        self.gpioStart = Button(gpioStart)
        self.gpioRead = Button(gpioRead)

        self.startPressed = False
        self.readPressed = False

    def ifStartPressed(self):
        if self.gpioStart.is_pressed and not self.startPressed:
            self.startPressed = True
        elif not self.gpioStart.is_pressed and self.startPressed:
            self.startPressed = False
            return True
        return False
    
    def ifReadPressed(self):
        if self.gpioRead.is_pressed and not self.readPressed:
            self.readPressed = True
        elif not self.gpioRead.is_pressed and self.readPressed:
            self.readPressed = False
            return True
        return False
    
    def readPotentiometer(self):
        return self.gpioPot.value