import unittest
from gpiozero.pins.mock import MockFactory
from gpiozero import Device
import threading
from model.platine import Platine
from model.model import Model

Device.pin_factory = MockFactory()

class TestBouton(unittest.TestCase):
    def setUp(self):
        self.platine = Platine(21, 20)
        self.model = Model(21, 20, None)

    def test_bouton_start_normal(self):
        self.threadStart = threading.Thread(target=self.model.start, daemon=True)
        self.threadStart.start()
        
        self.platine.gpioStart.pin.drive_high()
        self.platine.gpioStart.pin.drive_low()
        self.assertTrue(self.platine.ifStartPressed())
        
        self.model.stoppingProgram = True

    def test_bouton_start_pressed(self):
        self.threadStart = threading.Thread(target=self.model.start, daemon=True)
        self.threadStart.start()
        
        self.platine.gpioStart.pin.drive_high()
        self.assertFalse(self.platine.ifStartPressed())
        
        self.model.stoppingProgram = True
    
    def test_bouton_start_not_pressed(self):
        self.threadStart = threading.Thread(target=self.model.start, daemon=True)
        self.threadStart.start()
        
        self.platine.gpioStart.pin.drive_low()
        self.assertFalse(self.platine.ifStartPressed())
        
        self.model.stoppingProgram = True

    def test_bouton_read_normal(self):
        self.threadRead = threading.Thread(target=self.model.read, daemon=True)
        self.threadRead.start()
        
        self.platine.gpioRead.pin.drive_high()
        self.platine.gpioRead.pin.drive_low()
        self.assertTrue(self.platine.ifReadPressed())
        
        self.model.stoppingProgram = True

    def test_bouton_read_pressed(self):
        self.threadRead = threading.Thread(target=self.model.read, daemon=True)
        self.threadRead.start()
        
        self.platine.gpioRead.pin.drive_high()
        self.assertFalse(self.platine.ifReadPressed())
        
        self.model.stoppingProgram = True

    def test_bouton_read_not_pressed(self):
        self.threadRead = threading.Thread(target=self.model.read, daemon=True)
        self.threadRead.start()
        
        self.platine.gpioRead.pin.drive_low()
        self.assertFalse(self.platine.ifReadPressed())
        
        self.model.stoppingProgram = True

if __name__ == '__main__':
    unittest.main()