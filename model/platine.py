from gpiozero import MCP3008, Button

class Platine:
    def __init__(self, gpioStart, gpioRead):
        self.gpioPot = MCP3008(channel=0)
        self.gpioStart = Button(gpioStart)
        self.gpioRead = Button(gpioRead)
    
    def read_potentiometer(self):
        return self.gpioPot.value