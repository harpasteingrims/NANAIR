class GetIAAD():
    def __init__(self, ioapi):
        self.ioapi = ioapi

    def list_available_emp_by_date(self, user_input_date):
        employee_list = self.ioapi.get_list_of_all_employees()
        voyage_list = self.ioapi.get_all_voyages_list()
        for time_object in voyage_list:
            available_emps_for_selected_day = []
            if time_object.time == user_input_date:
                pass  #Hvernig er best að tengja saman employees og ferðirnar þeirra?

    def list_unavailable_emp_by_date(self, user_input_date):
        employee_list = self.ioapi.get_list_of_all_employees()
        voyage_list = self.ioapi.get_all_voyages_list()
        for time_object in voyage_list:
            unavailable_emps_for_selected_day = []
            if time_object.time == user_input_date:
                pass  #Hvernig er best að tengja saman employees og ferðirnar þeirra?
        #Sennilega best að kalla bara á neðsta listann hérna
        pass

    def list_airplane_status_by_date(self, user_input_date):
        airplane_list = self.ioapi.get_airplane_list

        pass #Líka pæling hérna hvar er best að geyma þessar upplýsingar og hvernig er best að ná í þær og vinna úr þeim

    def list_voyages_status_by_date(self, user_input_date):
        voyage_list = self.ioapi.get_all_voyages_list()
        for voyage in voyage_list:
            voyages__for_selected_day = []

        pass