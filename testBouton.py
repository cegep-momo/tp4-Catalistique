import unittest
from gpiozero.pins.mock import MockFactory
from gpiozero import Device
import threading
from model.model import Model

Device.pin_factory = MockFactory()

class TestBouton(unittest.TestCase):

    def setUp(self):
        self.model = Model(21, 20, None)

    def tearDown(self):
        self.model.stoppingProgram = True
        if hasattr(self, 'threadStart') and self.threadStart.is_alive():
            self.threadStart.join()
        if hasattr(self, 'threadRead') and self.threadRead.is_alive():
            self.threadRead.join()
        self.model = None

    def test_bouton_start_normal(self):
        self.threadStart = threading.Thread(target=self.model.start, daemon=True)
        self.threadStart.start()
        
        self.model.platine.gpioStart.pin.drive_low()
        self.model.platine.ifStartPressed()
        self.model.platine.gpioStart.pin.drive_high()
        
        self.assertTrue(self.model.platine.ifStartPressed())

    def test_bouton_start_pressed(self):
        self.threadStart = threading.Thread(target=self.model.start, daemon=True)
        self.threadStart.start()
        
        self.model.platine.gpioStart.pin.drive_low()
        self.assertFalse(self.model.platine.ifStartPressed())

    def test_bouton_start_not_pressed(self):
        self.threadStart = threading.Thread(target=self.model.start, daemon=True)
        self.threadStart.start()
        
        self.model.platine.gpioStart.pin.drive_high()
        self.assertFalse(self.model.platine.ifStartPressed())

    def test_bouton_read_normal(self):
        self.threadRead = threading.Thread(target=self.model.read, daemon=True)
        self.threadRead.start()
        
        self.model.platine.gpioRead.pin.drive_low()
        self.model.platine.ifReadPressed()
        self.model.platine.gpioRead.pin.drive_high()
        self.assertTrue(self.model.platine.ifReadPressed())

    def test_bouton_read_pressed(self):
        self.threadRead = threading.Thread(target=self.model.read, daemon=True)
        self.threadRead.start()
        
        self.model.platine.gpioRead.pin.drive_high()
        self.assertFalse(self.model.platine.ifReadPressed())

    def test_bouton_read_not_pressed(self):
        self.threadRead = threading.Thread(target=self.model.read, daemon=True)
        self.threadRead.start()
        
        self.model.platine.gpioRead.pin.drive_low()
        self.assertFalse(self.model.platine.ifReadPressed())

if __name__ == '__main__':
    unittest.main()