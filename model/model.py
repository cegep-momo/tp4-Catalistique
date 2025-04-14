from .platine import Platine
import threading, time, datetime, json

class Model:
    def __init__(self, gpioStart, gpioRead):
        self.platine = Platine(gpioStart, gpioRead)
        self.started = False
        self.stoppingProgram = False

    def start_thread_start(self):
        self.threadStart = threading.Thread(target=self.start, daemon=True)
        self.threadStart.start()

    def start_thread_read(self):
        self.threadRead = threading.Thread(target=self.read, daemon=True)
        self.threadRead.start()

    def start(self):
        while True and not self.stoppingProgram:
            if self.started:
                self.update()
                if self.platine.ifStartPressed():
                    self.started = False
            else:
                if self.platine.ifStartPressed():
                    self.started = True
            time.sleep(0.1)
    
    def read(self):
        print("")

    def update(self):
        self.potValue = self.platine.read_potentiometer()

        return self.potValue
    
    def saveReading(self):
        if self.started:
            now = datetime.datetime.now()
            filename = "readings.json"
            data = {
                "timestamp": now.strftime("%Y-%m-%d %H:%M:%S"),
                "value": self.potValue
            }
            try:
                with open(filename, "r") as file:
                    readings = json.load(file)
            except FileNotFoundError:
                with open(filename, "w") as file:
                    readings = []
                    json.dump(readings, file, indent=4)
            finally:
                with open(filename, "w") as file:
                    readings.append(data)
                    json.dump(readings, file, indent=4)