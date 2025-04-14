from datetime import datetime

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