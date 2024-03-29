class DestinationsModel():
    def __init__(self, country, airport, flight_dur_from_Ice, dist_from_Ice, contact_name, contact_phone_number, destiID):
        self.country = country
        self.airport = airport
        self.flight_dur_from_Ice = flight_dur_from_Ice
        self.dist_from_Ice = dist_from_Ice
        self.contact_name = contact_name
        self.contact_phone_number = contact_phone_number
        self.destiID = destiID
    
    def print_destinations(self, str_infront):
        return f"\n{str_infront} {self.country}, {self.airport}, {self.flight_dur_from_Ice}, {self.dist_from_Ice}, {self.contact_name}, {self.contact_phone_number}, {self.destiID}"
    
    def print_emergency(self):
        return f"\n{self.country}´s emergency contact in {self.airport}: \n\nName: {self.contact_name}\nNumber: {self.contact_phone_number}"