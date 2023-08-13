#Joshua Dalida, Camilla Molines
#Aug 11, 2023
#This program is a management system for a hospitals doctors and patients.
#it allows users to manage doctors and patients information
#this allows the hospital to have a menu system for their managing system 


#sets the doctor class
class Doctor:
    def __init__(
        self, doctor_id, name, specialization, working_time, qualification, room_number
    ):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.working_time = working_time
        self.qualification = qualification
        self.room_number = room_number

    def __str__(self):
        return "{:<5} {:<20} {:<15} {:<15} {:<15} {:<10}".format(
            self.doctor_id,
            self.name,
            self.specialization,
            self.working_time,
            self.qualification,
            self.room_number,
        )

    # Getters
    def get_doctor_id(self):
        return self.doctor_id

    def get_name(self):
        return self.name

    def get_specialization(self):
        return self.specialization

    def get_working_time(self):
        return self.working_time

    def get_qualification(self):
        return self.qualification

    def get_room_number(self):
        return self.room_number

    # Setters
    def set_name(self, new_name):
        self.name = new_name

    def set_specialization(self, new_specialization):
        self.specialization = new_specialization

    def set_working_time(self, new_working_time):
        self.working_time = new_working_time

    def set_qualification(self, new_qualification):
        self.qualification = new_qualification

    def set_room_number(self, new_room_number):
        self.room_number = new_room_number


#all the management functions for doctors
class DoctorManager:
    doctors_list = []

    def __init__(self):
        self.read_doctors_file()

    def format_dr_info(self, doctor):
        return str(doctor)
        
#takes in the doctors info and retuns it to the doctor class
    def enter_dr_info(self):
        doctor_id = input("\nEnter the doctor's ID: ")
        name = input("Enter the doctor's Name: ")
        specialization = input("Enter the doctor's Specialization: ")
        working_time = input("Enter the doctor’s timing (e.g., 7am-10pm): ")
        qualification = input("Enter the doctor’s qualification: ")
        room_number = input("Enter the doctor’s room number: ")
        return Doctor(
            doctor_id, name, specialization, working_time, qualification, room_number
        )
        
#reads the doctor.txt and puts it into the doctors list
    def read_doctors_file(self):
        self.doctors_list = []
        with open("doctors.txt", "r") as file:
            lines = file.readlines()[1:]
            for line in lines:
                doctor_info = line.strip().split("_")
                if len(doctor_info) == 6:
                    doctor = Doctor(*doctor_info)
                    self.doctors_list.append(doctor)
                    
#takes in the doctors id search and checks if its there is something in the doctors list
    def search_doctor_by_id(self, doctor_id_search):
        for doctor in self.doctors_list:
            if doctor.doctor_id == doctor_id_search:
                return doctor
                
#takes in the doctors name search and checks if its there is something in the doctors list
    def search_doctor_by_name(self, doctor_name_search):
        found_doctors = []
        for doctor in self.doctors_list:
            if doctor.name.lower() == doctor_name_search.lower():
                found_doctors.append(doctor)
        return found_doctors

#takes in the doctors class displays the doctors information
    def display_doctor_info(self, doctor):
        print("Doctor Information:")
        print(doctor)

#writes in the selected doctors line the new information
    def write_list_of_doctors_to_file(self):
            with open("doctors.txt", "w") as file:
                for doctor in self.doctors_list:
                    file.write(
                        f"{doctor.doctor_id}_{doctor.name}_{doctor.specialization}_{doctor.working_time}_{doctor.qualification}_{doctor.room_number}\n")

#takes in that doctors id and edits the infromation using the users input then uses the write list of doctors to file function    
    def edit_doctor_info(self, doctor_id):
        found_doctor = self.search_doctor_by_id(doctor_id)
        if found_doctor:
            # Update doctor's information
            found_doctor.set_name(input("Enter new Name: "))
            found_doctor.set_specialization(input("Enter new Specialization: "))
            found_doctor.set_working_time(input("Enter new Timing: "))
            found_doctor.set_qualification(input("Enter new Qualification: "))
            found_doctor.set_room_number(input("Enter new Room Number: "))

            print(f"\nDoctor whose ID is {doctor_id} has been edited")

            self.write_list_of_doctors_to_file()

#gets the doctors list and prints all of their info in the space given
    def display_doctors_list(self):
        if self.doctors_list:
            print(
                "{:<5} {:<20} {:<15} {:<15} {:<15} {:<10}".format(
                    "Id", "Name", "Speciality", "Timing", "Qualification", "Room Number"
                )
                + "\n"
            )
            for doctor in self.doctors_list:
                print(str(doctor) + "\n")

#takes in the news doctors information and writes it in the doctors.txt file in the format needed 
    def add_doctor_to_file(self, doctor):
        self.doctors_list.append(doctor)
        with open("doctors.txt", "a") as file:
            file.write(
                f"\n{doctor.doctor_id}_{doctor.name.replace(' ', '_')}_{doctor.specialization}_{doctor.working_time.replace('-', '').lower()}_{doctor.qualification}_{doctor.room_number}\n"
            )
        print(f"\nDoctor whose ID is {doctor.doctor_id} has been added")

#sets up the patient class
class Patient:
    def __init__(self, pid, name, disease, gender, age):
        self.pid = pid
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age

    def __str__(self):
        return "{:<5} {:<20} {:<15} {:<10} {:<5}".format(
            self.pid, self.name, self.disease, self.gender, self.age
        )

    # Getters
    def get_pid(self):
        return self.pid

    def get_name(self):
        return self.name

    def get_disease(self):
        return self.disease

    def get_gender(self):
        return self.gender

    def get_age(self):
        return self.age

    # Setters
    def set_name(self, new_name):
        self.name = new_name

    def set_disease(self, new_disease):
        self.disease = new_disease

    def set_gender(self, new_gender):
        self.gender = new_gender

    def set_age(self, new_age):
        self.age = new_age

#all the functions to manage the patients infromation
class PatientManager:
    patients_list = []

    def __init__(self):
        self.read_patients_file()

    def format_patient_info_for_file(self, patient):
        return "{:<5} {:<20} {:<15} {:<10} {:<5}".format(
            patient.get_pid(),
            patient.get_name(),
            patient.get_disease(),
            patient.get_gender(),
            patient.get_age(),
        )

#takes in all the patients information and returns it in order needed    
    def enter_patient_info(self):
        pid = input("\nEnter Patient id: ")
        name = input("Enter Patient name: ")
        disease = input("Enter Patient disease: ")
        gender = input("Enter Patient gender: ")
        age = input("Enter Patient age: ")
        return Patient(pid, name, disease, gender, age)

#opens the patients.txt file and puts each line into a list in the order needed
    def read_patients_file(self):
        self.patients_list = []
        with open("patients.txt", "r") as file:
            lines = file.readlines()[1:]
            for line in lines:
                patient_info = line.strip().split("_")
                if len(patient_info) == 5:
                    patient = Patient(*patient_info)
                    self.patients_list.append(patient)

#takes in the pid from the user and if it is the same as one in the list then it will return the patients class
    def search_patient_by_id(self, pid_search):
        for patient in self.patients_list:
            if patient.get_pid() == pid_search:
                return patient

#displays the patients information in order and in the space given
    def display_patient_info(self, patient):
        print("Patient Information:")
        print(patient)

#takes in the patients list and writes it into the patients.txt file    
    def write_list_of_patients_to_file(self):
        with open("patients.txt", "w") as file:
            for patient in self.patients_list:
                file.write(f"{patient.pid} {patient.name}_{patient.disease}_{patient.gender}_{patient.age}\n")

#takes in the patients id then if it is the same as one in the list, it will take in the infromation from the user the uses the write list of parients to file
    def edit_patient_info(self, patient_id):
        found_patient = self.search_patient_by_id(patient_id)

        if found_patient:
            # Update patient's information
            found_patient.set_name(input("Enter new Name: "))
            found_patient.set_disease(input("Enter new disease: "))
            found_patient.set_gender(input("Enter new gender: "))
            found_patient.set_age(input("Enter new age: "))
            print(f"\nPatient whose ID is {patient_id} has been edited.")

            self.write_list_of_patients_to_file()

#prints all the patients information in the space needed    
    def display_patients_list(self):
        if self.patients_list:
            print(
                "{:<5} {:<20} {:<15} {:<10} {:<5}".format(
                    "ID", "Name", "Disease", "Gender", "Age"
                )
                + "\n"
            )
            for patient in self.patients_list:
                print(str(patient) + "\n")

#takes patients information then adds it to the patients.txt file in the format needed    
    def add_patient_to_file(self, patient):
        self.patients_list.append(patient)
        with open("patients.txt", "a") as file:
            formatted_info = f"\n{patient.pid}_{patient.name.replace(' ', '_')}_{patient.disease}_{patient.gender}_{patient.age}\n"
            file.write(formatted_info)
        print(f"\nPatient whose ID is {patient.pid} has been added.")

#all the functions to handle the menu and mangement of doctors and patients
class Management:
    def __init__(self):
        self.doctor_manager = DoctorManager()
        self.patient_manager = PatientManager()

#the directory for doctors and patients or exit     
    def display_menu(self):
        while True:
            print("Welcome to Alberta Hospital (AH) Management system")
            print("Select from the following options, or select 3 to stop: ")
            print("1 - Doctors")
            print("2 - Patients")
            print("3 - Exit")
            selection = input(">>> ")

            if selection == "1":
                self.display_doctors_menu()
            elif selection == "2":
                self.display_patients_menu()
            elif selection == "3":
                print("Thanks for using the program. Bye!")
                break

#the directory for doctors managment
    def display_doctors_menu(self):
        while True:
            print("\nDoctors Menu:")
            print("1 - Display Doctors list")
            print("2 - Search for doctor by ID")
            print("3 - Search for doctor by name")
            print("4 - Add doctor")
            print("5 - Edit doctor info")
            print("6 - Back to Main Menu")
            doctors_selection = input(">>> ")

            #if user enters 1 then run doctor_manager.display_doctors_list()
            if doctors_selection == "1":
                self.doctor_manager.display_doctors_list()
                
            #if user enters 2 then ask for what doctors id then run doctor_manager.search_doctor_by_id with that doctors id then print it to the user, if there is no match it will it cant find doctor
            elif doctors_selection == "2":
                doctor_id = input("\nEnter the doctor Id:")
                found_doctor = self.doctor_manager.search_doctor_by_id(doctor_id)
                if found_doctor:
                    print(
                        "\n"
                        + "{:<5} {:<20} {:<15} {:<15} {:<15} {:<10}".format(
                            "Id",
                            "Name",
                            "Speciality",
                            "Timing",
                            "Qualification",
                            "Room Number",
                        )
                        + "\n"
                    )
                    print(str(found_doctor))
                else:
                    print("Can't find the doctor with the same ID on the system")

            #if user enters 3 it will ask for the doctors name, then run doctor_manager.search_doctor_by_name using the doctors name if there is a match it will print it to user, if not it'll say there is no doctor
            elif doctors_selection == "3":
                doctor_name = input("\nEnter Doctor name: ")
                found_doctors = self.doctor_manager.search_doctor_by_name(doctor_name)
                if found_doctors:
                    print(
                        "\n"
                        + "{:<5} {:<20} {:<15} {:<15} {:<15} {:<10}".format(
                            "Id",
                            "Name",
                            "Speciality",
                            "Timing",
                            "Qualification",
                            "Room Number",
                        )
                        + "\n"
                    )
                    for doctor in found_doctors:
                        print(str(doctor))
                else:
                    print("Can't find the doctor with the same name on the system")

            #if users enters 4 it takes in the doctors infromation using doctor_manager.enter_dr_info() then uses doctor_manager.add_doctor_to_file to add it to the doctor.txt file
            elif doctors_selection == "4":
                new_doctor = self.doctor_manager.enter_dr_info()
                self.doctor_manager.add_doctor_to_file(new_doctor)

            #if the user enters 5 it'll ask for the doctors id and see if there is a doctor that matches by using doctor_manager.search_doctor_by_id, if there is one that matches then it will run .doctor_manager.edit_doctor_info to edit their information
            elif doctors_selection == "5":
                doctor_id = input(
                    "\nPlease enter the id of the doctor that you want to edit their information: "
                )
                found_doctor = self.doctor_manager.search_doctor_by_id(doctor_id)
                if found_doctor:
                    self.doctor_manager.edit_doctor_info(doctor_id)
                else:
                    print("Doctor not found.")
            elif doctors_selection == "6":
                break

    #patients directory
    def display_patients_menu(self):
        while True:
            print("\nPatients Menu:")
            print("1 - Display patients list")
            print("2 - Search for patient by ID")
            print("3 - Add patient")
            print("4 - Edit patient info")
            print("5 - Back to Main Menu")
            patients_selection = input(">>> ")

            #if the user inputs 1 then it will diplay the all the patients using patient_manager.display_patients_list()
            if patients_selection == "1":
                self.patient_manager.display_patients_list()
                
            #
            elif patients_selection == "2":
                pid = input("\nEnter Patient Id: ")
                found_patient = self.patient_manager.search_patient_by_id(pid)
                if found_patient:
                    print(
                        "\n"
                        + "{:<5} {:<20} {:<15} {:<10} {:<5}".format(
                            "ID", "Name", "Disease", "Gender", "Age"
                        )
                        + "\n"
                    )
                    print(str(found_patient) + "\n")
                else:
                    print("Can't find the Patient with the same id on the system")

            #if user inputs 3 the it asks for the patients info using patient_manager.enter_patient_info() then adds it to the patient.txt file 
            elif patients_selection == "3":
                new_patient = self.patient_manager.enter_patient_info()
                self.patient_manager.add_patient_to_file(new_patient)

            #if user inputs 4 then takes an id from the user, then checks if its exsits using patient_manager.search_patient_by_id, if it does then it edits it using patient_manager.edit_patient_info
            elif patients_selection == "4":
                pid = input(
                    "\nPlease enter the id of the Patient that you want to edit their information: "
                )
                found_patient = self.patient_manager.search_patient_by_id(pid)
                if found_patient:
                    self.patient_manager.edit_patient_info(pid)

            #if 5 exits out of the patients directory
            elif patients_selection == "5":
                break


# runs the display menu
management_system = Management()
management_system.display_menu()
