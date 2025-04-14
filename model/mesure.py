from datetime import datetime
import json

class Mesure:
    def __init__(self, date_time: datetime, values: list):
        """
        Initializes a Mesure instance with a timestamp and a list of values.

        Args:
            date_time (datetime): The date and time of the measurement.
            values (list): A list of measured values.
        """
        self.date_time = date_time
        self.values = values

    def __repr__(self):
        """
        Returns a string representation of the Mesure instance.

        Returns:
            str: A string showing the date, time, and values of the measurement.
        """
        return f"Mesure(date_time={self.date_time}, values={self.values})"

    def afficherMesure(self):
        """
        Prints the measurement details, including the date, time, and values.
        """
        print(f"Date et heure: {self.date_time}")
        print("Valeur des mesures:")
        for value in self.values:
            print(f" - {value}")

    def saveReading(self):
        """
        Saves the measurement to a JSON file named 'readings.json'.
        If the file does not exist, it creates a new one.

        The data is appended to the existing list of readings in the file.
        """
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