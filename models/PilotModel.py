class PilotsModel():
    def __init__(self, SSN, name, role, rank, license_type, address, mobile_number, email):
        self.SSN = SSN 
        self.name = name
        self.role = role
        self.rank = rank
        self.license_type = license_type
        self.address = address
        self.mobile_number = mobile_number
        self.email = email
        
    def to_csv_string(self):
        return f"{self.SSN},{self.name},{self.role},{self.rank},{self.license_type},{self.address},{self.mobile_number},{self.email}"

    def print_pilot_info(self):
        return f"Name: {self.name} \nRole: {self.role} \nSSN: {self.SSN} \nAdress: {self.address} \nMobile number: {self.mobile_number} \nEmail:{self.email}License type: {self.license_type}"


