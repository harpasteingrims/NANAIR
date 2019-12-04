from UI_folder.UImanager import UImanager
from models.CabinCrewModel import CabinCrewModel

class CabincrewUI():
    LENGTH_STAR = 20
    def __init__(self, llapi):
        self.llapi = llapi

    def show_cabincrew_menu(self):
        print(self.LENGTH_STAR * "*")
        print("CABIN CREW MENU \n\n1 Search for a cabin crew member \n2 Print overview of cabin crew \n3 Create a new cabin crew member\nB Back\n")

        action_str = input("Choose action: ").lower()
        print()

        if action_str == "1":
            self.show_enter_name_to_search()

        elif action_str == "2":
            self.show_cabincrew_member_overview()

        elif action_str == "3":
            self.show_cabincrew_member_create_form()

        elif action_str == "b":
            return

    def show_enter_name_to_search(self):
        print("Search for a cabin crew member to get information")

        name = input("Enter name of cabincrew member: ")
        print()

        print("1 {}'s flight schedule".format(name))
        print("2 Edit information about cabin crew member \nB Back")

        action_str = input("Choose action: ").lower()
        print()

        if action_str == "1":
            self.show_flight_schedule_of_cabincrew_member()

        elif action_str == "2":
            self.show_cabincrew_member_edit_form()

        elif action_str == "b":
            return

    def show_flight_schedule_of_cabincrew_member(self):
        data_from = input("Enter date from: ")
        date_to = input("Enter date to: ")

        print("B Back")

        action_str = input("Choose action: ").lower()
        print()

        if action_str == "b":
            return
    
    def show_cabincrew_member_edit_form(self):
        new_address = input("Enter new address")
        new_mobile_number = input("Enter new mobile number: ")
        new_email = input("Enter new email: ")

        print("S Save \nB Back\n")

        action_str = input("Choose action: ").lower()
        print()

        if action_str == "s":
            print("cabin crew member's information successfully changed")
            return

        elif action_str == "b":
            return

    def show_cabincrew_member_overview(self):
        print("OVERVIEW OF CABIN VREW\n")
        cabin_crew = self.llapi.get_cabin_crew_overview()
        print(cabin_crew)
        
        print("B Back\n")

        action_str = input("Choose action: ").lower()
        print()

        if action_str == "b":
            return

    
    def show_cabincrew_member_create_form(self):

        print("CREATE A NEW CABIN CREW MEMBER\n")
        name = input("Enter full name: ")
        role = input("Enter role: ")
        ssn = input("Enter social security number: ")
        address = input("Enter address: ")
        mobile_number = input("Enter mobile number: ")
        email = input("Enter email: ")

        #new_cabincrew_member = CabinCrewModel(name, role, ssn, address, mobile_number, email)

        print("\nS Save \nB Back \n")

        action_str = input("Choose action: ").lower()
        print()

        if action_str == "s":
            print("Cabin crew member successfully created\n")
            return

        elif action_str == "b":
            return