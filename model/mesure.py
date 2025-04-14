from datetime import datetime
import json

class Mesure:
    def __init__(self, date_time: datetime, values: list):
        self.date_time = date_time
        self.values = values

    def __repr__(self):
        return f"Mesure(date_time={self.date_time}, values={self.values})"

    def afficherMesure(self):
        print(f"Date et heure: {self.date_time}")
        print("Valeur des mesures:")
        for value in self.values:
            print(f" - {value}")

    def saveReading(self):
        filename = "readings.json"
        data = {
            "date_time": self.date_time.strftime("%Y-%m-%d %H:%M:%S"),
            "values": self.values
        }
        try:
            with open(filename, "r") as file:
                readings = json.load(file)
        except FileNotFoundError:
            readings = []
        readings.append(data)
        with open(filename, "w") as file:
            json.dump(readings, file, indent=4)