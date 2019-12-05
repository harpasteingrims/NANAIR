import csv
from models.CabinCrewModel import CabinCrewModel
from models.PilotModel import PilotsModel
from models.AirplanesModel import AirplanesModel
from models.VoyagesModel import VoyagesModel
from models.DestinationsModel import DestinationsModel

class CreateIO():
    def __init__(self, get):
        self.get = get
        
    def add_pilot(self, new_pilot):
        with open('Pilots.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(new_pilot.to_csv_string())

    def add_cabincrew(self, new_cabincrew):
        with open('Pilots.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(new_cabincrew.to_csv_string())
        
    def add_airplane(self, new_airplane):
        with open('Aircraft.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(new_airplane.to_csv_string())

    def add_destiantions(self, new_destination):
        with open('Destinations.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(new_destination.to_csv_string())

    def add_voyage(self, new_voyage):
        with open('Voyages.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(new_voyage.to_csv_string())