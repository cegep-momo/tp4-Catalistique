from view import LCD1602

class View:
    def __init__(self):
        self.controler = None
        self.lcd = LCD1602.CharLCD1602()
        self.lcd.init_lcd(0x27, 1)

    def setControler(self, controler):
        self.controler = controler

    def update(self, potValue):
        self.lcd.clear()
        self.lcd.write(0, 0, "Potentiometer:")
        self.lcd.write(1, 1, f"{potValue:.4f}")

    def readingsOffScreen(self):
        self.lcd.clear()
        self.lcd.write(0, 0, "Press start")
        self.lcd.write(1, 1, "Waiting...")

    def cleanup(self):
        self.lcd.clear()