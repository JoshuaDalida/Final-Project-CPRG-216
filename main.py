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

    # Getters#
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

    # getters##
    def set_name(self, new_name):
        self.new_name = new_name
        self.name = self.new_name

    def set_specialization(self, new_specialization):
        self.new_specialization = new_specialization
        self.specialization = self.new_specialization

    def set_working_time(self, new_working_time):
        self.new_working_time = new_working_time
        self.working_time = new_working_time

    def set_qualification(self, new_qualification):
        self.new_qualification = new_qualification
        self.qualification = self.new_qualification

    def set_room_number(self, new_room_number):
        self.new_room_number = new_room_number
        self.room_number = self.new_room_number


class DoctorManager:
    doctors_list = []

    def __init__(self):
        self.read_doctors_file()

    def format_dr_info(self, doctor):
        return str(doctor)

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

    def read_doctors_file(self):
        self.doctors_list = []
        with open("doctors.txt", "r") as file:
            lines = file.readlines()[1:]
            for line in lines:
                doctor_info = line.strip().split("_")
                if len(doctor_info) == 6:
                    doctor = Doctor(*doctor_info)
                    self.doctors_list.append(doctor)

    def search_doctor_by_id(self, doctor_id_search):
        for doctor in self.doctors_list:
            if doctor.doctor_id == doctor_id_search:
                return doctor

    def search_doctor_by_name(self, doctor_name_search):
        found_doctors = []
        for doctor in self.doctors_list:
            if doctor.name.lower() == doctor_name_search.lower():
                found_doctors.append(doctor)
        return found_doctors

    def display_doctor_info(self, doctor):
        print("Doctor Information:")
        print(doctor)

    def edit_doctor_info(self, doctor_id):
        self.doctor_id = doctor_id
        found_doctor = self.search_doctor_by_id(doctor_id)
        if found_doctor:
            # Update doctor's information
            found_doctor.set_name(input("Enter new Name: "))
            found_doctor.set_specialization(input("Enter new Specialization: "))
            found_doctor.set_working_time(input("Enter new Working Time: "))
            found_doctor.set_qualification(input("Enter new Qualification: "))
            found_doctor.set_room_number(input("Enter new Room Number: "))

            print(f"\nDoctor whose ID is {doctor_id} has been edited\n")

        else:
            print("Doctor not found.")

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

    def write_list_of_doctors_to_file(self):
        with open("doctors.txt", "w") as file:
            for doctor in self.doctors_list:
                file.write(self.format_dr_info(doctor) + "\n")
        print("List of doctors written to file successfully.")

    def add_doctor_to_file(self, doctor):
        self.doctors_list.append(doctor)
        with open("doctors.txt", "a") as file:
            file.write(
                f"\n{doctor.doctor_id}_{doctor.name.replace(' ', '_')}_{doctor.specialization}_{doctor.working_time.replace('-', '').lower()}_{doctor.qualification}_{doctor.room_number}\n"
            )
        print(f"\nDoctor whose ID is {doctor.doctor_id} has been added\n")


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

    def set_name(self, new_name):
        self.name = new_name

    def set_disease(self, new_disease):
        self.disease = new_disease

    def set_gender(self, new_gender):
        self.gender = new_gender

    def set_age(self, new_age):
        self.age = new_age


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

    def enter_patient_info(self):
        pid = input("Enter Patient ID: ")
        name = input("Enter Name: ")
        disease = input("Enter Disease: ")
        gender = input("Enter Gender: ")
        age = input("Enter Age: ")
        return Patient(pid, name, disease, gender, age)

    def read_patients_file(self):
        self.patients_list = []
        try:
            with open("patients.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    patient_info = line.strip().split("_")
                    if len(patient_info) == 5:
                        patient = Patient(*patient_info)
                        self.patients_list.append(patient)
        except FileNotFoundError:
            print("Patients file not found. Creating an empty list.")

    def search_patient_by_id(self, pid_search):
        for patient in self.patients_list:
            if patient.get_pid() == pid_search:
                return patient

    def display_patient_info(self, patient):
        print("Patient Information:")
        print(patient)

    def edit_patient_info(self, patient_id):
        found_patient = self.search_patient_by_id(patient_id)

        if found_patient:
            print("Found patient:")
            self.display_patient_info(found_patient)

            # Get new values for the patient
            new_name = input("Enter new Name: ")
            new_disease = input("Enter new Disease: ")
            new_gender = input("Enter new Gender: ")
            new_age = input("Enter new Age: ")

            # Update patient's information
            found_patient.set_name(new_name)
            found_patient.set_disease(new_disease)
            found_patient.set_gender(new_gender)
            found_patient.set_age(new_age)

            self.write_list_of_patients_to_file()
            print("Patient information updated successfully.")
        else:
            print("Patient not found.")

    def display_patients_list(self):
        if self.patients_list:
            print("List of Patients:")
            print(
                "{:<5} {:<20} {:<15} {:<10} {:<5}".format(
                    "ID", "Name", "Disease", "Gender", "Age"
                )
            )
            for patient in self.patients_list:
                print(patient)
        else:
            print("No patients found.")

    def write_list_of_patients_to_file(self):
        with open("patients.txt", "w") as file:
            for patient in self.patients_list:
                file.write(self.format_patient_info_for_file(patient) + "\n")
            print("List of patients written to file successfully.")

    def add_patient_to_file(self, patient):
        self.patients_list.append(patient)
        with open("patients.txt", "a") as file:
            formatted_info = f"\n{patient.pid}_{patient.name.replace(' ', '_')}_{patient.disease}_{patient.gender}_{patient.age}\n"
            file.write(formatted_info)
        print(f"Patient with ID {patient.pid} has been added.")


class Management:
    def __init__(self):
        self.doctor_manager = DoctorManager()
        self.patient_manager = PatientManager()

    def display_menu(self):
        print("Welcome to Alberta Hospital (AH) Managment system")
        while True:
            print("Select from the following options:")
            print("1 - Doctors")
            print("2 - Patients")
            print("3 - Exit")
            selection = input(">>> ")

            if selection == "1":
                self.display_doctors_menu()
            elif selection == "2":
                self.display_patients_menu()
            elif selection == "3":
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please select a valid option.")

    def display_doctors_menu(self):
        while True:
            print("\nDoctors Menu:")
            print("1 - Display Doctors list")
            print("2 - Search for doctor by ID")
            print("3 - Search for doctor by name")
            print("4 - Add doctor")
            print("5 - Edit doctor info")
            print("6 - Back to Main Menu")
            doctors_selection = input(">>>")

            if doctors_selection == "1":
                self.doctor_manager.display_doctors_list()
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
                    print("Can't find the doctor with the same ID on the system\n")
            elif doctors_selection == "3":
                doctor_name = input("\nEnter Doctor Name: ")
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
                        print(str(doctor) + "\n ")
                else:
                    print("Can't find the doctor with the same name on the system\n")

            elif doctors_selection == "4":
                new_doctor = self.doctor_manager.enter_dr_info()
                self.doctor_manager.add_doctor_to_file(new_doctor)

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

    def display_patients_menu(self):
        while True:
            print("Select from the following options:")
            print("1 - Display Patients list")
            print("2 - Search for patient by ID")
            print("3 - Add patient")
            print("4 - Edit patient info")
            print("5 - Back to Main Menu")
            patients_selection = input(">>>")

            if patients_selection == "1":
                self.patient_manager.display_patients_list()
            elif patients_selection == "2":
                pid = input("Enter Patient ID to search: ")
                found_patient = self.patient_manager.search_patient_by_id(pid)
                if found_patient:
                    print(
                        "{:<5} {:<20} {:<15} {:<10} {:<5}".format(
                            "ID", "Name", "Disease", "Gender", "Age"
                        )
                    )
                    print(found_patient)
                else:
                    print("Patient not found.")
            elif patients_selection == "3":
                new_patient = self.patient_manager.enter_patient_info()
                self.patient_manager.add_patient_to_file(new_patient)
                print("Patient added successfully.")
            elif patients_selection == "4":
                pid = input("Enter Patient ID to edit: ")
                found_patient = self.patient_manager.search_patient_by_id(pid)
                if found_patient:
                    self.patient_manager.edit_patient_info(found_patient)
                    print("Patient information updated successfully.")
                else:
                    print("Patient not found.")
            elif patients_selection == "5":
                print("Returning to Main Menu.")
                break
            else:
                print("Invalid choice. Please select a valid option.")


# Usage
management_system = Management()
management_system.display_menu()
