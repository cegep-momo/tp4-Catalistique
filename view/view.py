from view import LCD1602

class View:
    def __init__(self):
        """
        Initializes the View class by setting up the LCD display and linking it to the controller.
        """
        self.controler = None
        self.lcd = LCD1602.CharLCD1602()
        self.lcd.init_lcd(0x27, 1)

    def setControler(self, controler):
        """
        Links the View to the given controller.

        Args:
            controler: The controller instance to link with the View.
        """
        self.controler = controler

    def update(self, potValue):
        """
        Updates the LCD display with the current potentiometer value.

        Args:
            potValue (float): The value of the potentiometer to display.
        """
        self.lcd.clear()
        self.lcd.write(0, 0, "Potentiometer:")
        self.lcd.write(1, 1, f"{potValue:.4f}")

    def readingsOffScreen(self):
        """
        Displays a message on the LCD indicating that the system is waiting for the start button to be pressed.
        """
        self.lcd.clear()
        self.lcd.write(0, 0, "Press start")
        self.lcd.write(1, 1, "Waiting...")

    def cleanup(self):
        """
        Clears the LCD display, typically called during cleanup or shutdown.
        """
        self.lcd.clear()