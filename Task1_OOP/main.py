# Main Program Entry
# Hospital Management System - Full OOP Implementation
# Functions: Menu, Patient, Doctor, Appointment, File Save


# Import classes
from patient import Patient
from patient import InPatient
from doctor import Doctor
from appointment import Appointment

# Function: Show system menu
def show_menu():
    """
    Show main menu
    """
    print(" HOSPITAL MANAGEMENT SYSTEM ")
    print("1. Add Inpatient")
    print("2. Add Regular Patient")
    print("3. Show All Patients")
    print("4. Show Doctor Info")
    print("5. Create Appointment")
    print("6. Show Appointments")
    print("7. Save Records To File")
    print("8. Exit System")


# Main Function
if __name__ == "__main__":

    # System initialization
    print("[System] System started successfully")
    print("[System] Loading data...")

    # Initialize doctor object
    doctor = Doctor("D001", "Li Ming", "General Surgery")
    print(f"[System] Default doctor loaded: {doctor.show_info()}")

    # List to store patients
    patient_list = []
    # List to store appointments
    appointment_list = []

    # Main loop
    while True:
        show_menu()
        # Get user input
        choice = input("\nPlease enter your choice (1-8):")
        
        # Option 1: Add Inpatient
        if choice == "1":
            print("\n--- [Add Inpatient] ---")
            pid = input("Enter patient ID ")
            name = input("Enter name")
            age = input("Enter age")
            gender = input("Enter gender (M/F) ")
            bed_no = input("Enter bed number ")

            inpatient = InPatient(pid, name, age, gender, bed_no)
            patient_list.append(inpatient)

            print("✅ Success: Inpatient added")


        # Option 2: Add Regular Patient

        elif choice == "2":
            print("\n--- [Add Regular Patient] ---")
            pid = input("Enter patient ID ")
            name = input("Enter name")
            age = input("Enter age")
            gender = input("Enter gender (M/F)")

            patient = Patient(pid, name, age, gender)
            patient_list.append(patient)

            print("✅ Success: Patient added")


        # Option 3: Show all patients
        elif choice == "3":
            print("\n--- [All Patient Information] ---")
            if len(patient_list) == 0:
                print("❌ No patient information")
            else:
                for index, patient in enumerate(patient_list, 1):
                    print(f"[{index}] {patient.show_info()}")

        # Option 4: Show doctor info
        elif choice == "4":
            print("\n--- [Doctor Information] ---")
            print(doctor.show_info())

        # Option 5: Create appointment
        elif choice == "5":
            print("\n--- [Create Appointment] ---")
            if len(patient_list) == 0:
                print("No patients, cannot create appointment")
                continue

            appt_id = input("Enter appointment ID ")
            time_str = input("Enter appointment time ")

            selected_patient = patient_list[-1]
            appt = Appointment(appt_id, selected_patient, doctor, time_str)
            appointment_list.append(appt)

            print("Success: Appointment created")


        # Option 6: Show all appointments
        elif choice == "6":
            print("\n--- [All Appointments] ---")
            if len(appointment_list) == 0:
                print("❌ No appointments / 暂无预约信息")
            else:
                for index, appt in enumerate(appointment_list, 1):
                    print(f"[{index}] {appt.show()}")

        # Option 7: Save records to file
        elif choice == "7":
            print("\n--- [Save To File] ---")
            try:
                with open("hospital_records.txt", "w", encoding="utf-8") as f:
                    f.write("=== HOSPITAL RECORDS ===\n")
             
                    f.write("[Patients]\n")
                    for p in patient_list:
                        f.write(p.show_info() + "\n")

                    f.write("\n[Appointments]\n")
                    for a in appointment_list:
                        f.write(a.show() + "\n")

                print("All records saved to hospital_records.txt")
            except:
                print("❌ Save failed")

        # Option 8: Exit system
        elif choice == "8":
            print("\n👋 Thank you for using the system")
            print("👋 System exiting")
            break
        # 无效输入
        # Invalid input
        # ------------------------------
        else:
            print("\n❌ Invalid choice, please enter 1-8")
