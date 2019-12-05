from models.PilotModel import PilotsModel
class PilotsUI():
    LENGTH_STAR = 20

    def __init__(self, llapi):
        self.llapi = llapi

    def show_pilot_menu(self):
        '''This prints the pilot menu'''

        action_str = ""
        while action_str != "q":
            print(self.LENGTH_STAR * "*")
            print("PILOT MENU")
            print("1 Search for a pilot")
            print("2 Print overview of pilots")
            print("3 Create a new pilot")
            print("B Back")
            print("Q Quit\n")
            action_str = input("Choose action: ").lower()
            print()

            if action_str == "1":
                self.show_enter_name_to_search()
            elif action_str == "2": 
                self.show_pilots_overview()
            elif action_str == "3": 
                self.show_pilot_create_form()
            elif action_str == "b":
                return     

    def show_enter_name_to_search(self):
        """This prints the search for a pilot window"""

        print(self.LENGTH_STAR * "*")
        print("SEARCH FOR A PILOT")
        
        name = input("Enter name of pilot: ").lower()
        print()
        
        pilot_info = self.llapi.get_info_about_pilot_by_name()
        print(pilot_info)
            #Name:
            #Role:
            #Social security number:
            #Adress:
            #Mobile number:
            #Email:
            #License type: 

        print("1 {}'s flight schedule").format(name)
        print("2 Edit information about pilot \nB Back")

        action_str = input("Choose action: ").lower()
        print()

        if action_str == "1":
            self.show_flight_schedule_of_pilot(name)

        elif action_str == "2": 
            self.show_pilot_edit_form(name)

        elif action_str == "b":
            self.show_pilot_menu()
    
    def show_flight_schedule_of_pilot(self, name):
        """Calls a class that makes a list of their voyages and prints it"""

        date_from = input("Enter date from: ")
        date_to = input("Enter date to: ")

        print(self.LENGTH_STAR * "*")
        #print("{}'S FLIGHT SCHEDULE").format(name.upper())
        flight_schedule = self.llapi.get_schedule_pilot_by_date()
        #Herna þarf name ad fara inn
        print("B Back")

        action_str = input("Choose action: ").lower()
        print()

        if action_str == "b":
            self.show_pilot_menu()

    def show_pilot_edit_form(self, name):
        """This prints the edit form for an employee"""
        
        print(self.LENGTH_STAR * "*")
        print("EDIT PILOT")
        # name, ssn, role.... = #calls the class to get the info of the pilot 
        #print("You are changing the information for pilot: {}, {}".format(name, ssn))
       
        new_address = input("Enter new address")
        new_mobile_number = input("Enter new mobile number: ")
        new_email = input("Enter new email: ")
        new_licence_type = input("Enter new license type: ")
        
        print("S Save \nB Back\n")

        action_str = input("Choose action: ").lower()
        print()

        if action_str == "s":
            #Takes the new info, changes and adds it to the pilot list
            #Calls the class that stores the info about the pilot to change it...
            print("Pilot's information successfully changed")
            self.show_pilot_menu()

        elif action_str == "b":
            self.show_pilot_menu()
     
    def show_pilots_overview(self):
        """This prints the overview of all pilots"""

        print(self.LENGTH_STAR * "*")
        print("OVERVIEW OF PILOTS\n")
        # Calls the class that makes a list of all pilots and prints it 
        pilots = self.llapi.get_pilot_overview()
        print(pilots)

        print("B Back\n")

        action_str = input("Choose action: ").lower()
        print()
        
        if action_str == "b":
            self.show_pilot_menu()
    
    def show_pilot_create_form(self):
        """This prints the create a pilot form"""

        print(self.LENGTH_STAR * "*")
        print("CREATE A NEW PILOT \n")
        name = input("Enter full name: ")
        role = input("Enter role: ")
        ssn = input("Enter social security number: ")
        address = input("Enter address: ")
        mobile_number = input("Enter mobile number: ")
        email = input("Enter email: ")
        license_type = input("Enter license type: ")
        
        print("\nS Save \nB Back\n")

        action_str = input("Choose action: ").lower()
        print()

        if action_str == "s":
            #Takes the info and adds it to the pilot list
            print("Pilot successfully created\n")
            #new_pilot = PilotModel(name, role, ssn, address, mobile_number, email, license_type)
            #self.pilot.create_pilot(new_pilot)
            #Hérna þurfum við að skella þessu í lista/dictionary og svo fara einn til baka eða lenda aftur á þessum skjá        
            self.show_pilot_menu()

        elif action_str == "b":
            self.show_pilot_menu()