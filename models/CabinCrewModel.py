class CabinCrewModel():
    def __init__(self, ssn, name, role, rank, address, mobile_number, email):
        self.ssn = ssn
        self.name = name
        self.role = role
        self.rank = rank
        self.address = address
        self.mobile_number = mobile_number
        self.email = email
    
    def to_csv_string(self):
        return f"{self.ssn}, {self.name}, {self.role}, {self.rank}, {self.address}, {self.mobile_number}, {self.email}"

    def print_crew_member_object_info(self):
        return f"Name: {self.name} \nRank: {self.rank} \nSSN: {self.ssn} \nAdress: {self.address} \nMobile number: {self.mobile_number} \nEmail:{self.email}"

    def print_crew_member_info_in_line(self, counter):
        return f"{counter} {self.name}, {self.ssn}, {self.role}, {self.rank}, {self.address}, {self.mobile_number}, {self.email}"

    def print_available_crew_info(self, counter):
        return f"\n{counter} {self.name}, {self.rank}"
