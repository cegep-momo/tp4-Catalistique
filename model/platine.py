from gpiozero import MCP3008, Button

class Platine:
    def __init__(self, gpioStart, gpioRead):
        """
        Initializes the Platine class with GPIO pins for the potentiometer, start button, and read button.

        Args:
            gpioStart (int): GPIO pin number for the start button.
            gpioRead (int): GPIO pin number for the read button.
        """
        self.gpioPot = MCP3008(channel=0)
        self.gpioStart = Button(gpioStart)
        self.gpioRead = Button(gpioRead)

        self.startPressed = False
        self.readPressed = False
        self.isReading = False

    def ifStartPressed(self):
        """
        Checks if the start button has been pressed and released.

        Returns:
            bool: True if the start button was pressed and released, False otherwise.
        """
        if self.gpioStart.is_pressed and not self.startPressed:
            self.startPressed = True
        elif not self.gpioStart.is_pressed and self.startPressed:
            self.startPressed = False
            return True
        return False
    
    def ifReadPressed(self):
        """
        Checks if the read button has been pressed and released.

        Returns:
            bool: True if the read button was pressed and released, False otherwise.
        """
        if self.gpioRead.is_pressed and not self.readPressed:
            self.readPressed = True
        elif not self.gpioRead.is_pressed and self.readPressed:
            self.readPressed = False
            return True
        return False
    
    def readPotentiometer(self):
        """
        Reads the current value of the potentiometer.

        Returns:
            float: The current potentiometer value as a float between 0 and 1.
        """
        return self.gpioPot.value * 3.3