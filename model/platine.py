from gpiozero import MCP3008, Button

class Platine:
    def __init__(self, gpioStart, gpioRead):
        self.gpioPot = MCP3008(channel=0)
        self.gpioStart = Button(gpioStart)
        self.gpioRead = Button(gpioRead)

        self.startPressed = False
        self.readPressed = 0

    def ifStartPressed(self):
        if self.gpioStart.is_pressed and self.startPressed == False:
            self.startPressed = True
        elif not self.gpioStart.is_pressed and self.startPressed == True:
            self.startPressed = False
            return True
        return False
    
    def read_potentiometer(self):
        return self.gpioPot.value