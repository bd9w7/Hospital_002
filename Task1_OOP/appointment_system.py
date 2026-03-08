from data_structures import Stack, Queue, BinarySearchTree, LinkedList
from patient_manager import Patient, PatientSorter

class AppointmentSystem:
    def __init__(self):
        # Initialize data structures
        self.__operation_stack = Stack()
        self.__normal_queue = Queue()
        self.__patient_bst = BinarySearchTree()
        self.__visit_history = LinkedList()
        self.__all_patients = []

    def register_patient(self, name, age, department, is_emergency=False, priority=5):
        # Create patient object
        patient = Patient(name, age, department, is_emergency, priority)

        self.__patient_bst.insert(patient.get_pid(), patient)

        if not is_emergency:
            self.__normal_queue.enqueue(patient)

        self.__all_patients.append(patient)
        self.__operation_stack.push(("register", patient.get_pid()))

        print(f"Patient registered successfully | {patient}")
        return patient.get_pid()

    def call_patient(self):
        # Process normal queue first (integrate Task2 min-heap for emergency priority later)
        if not self.__normal_queue.is_empty():
            patient = self.__normal_queue.dequeue()
            patient.set_status("treated")

            self.__operation_stack.push(("call", patient.get_pid()))

            self.__visit_history.add_at_end(patient)
            print(f"Patient called successfully | {patient}")
            return patient
        else:
            print("No patients waiting for treatment currently")
            return None

    def undo_operation(self):
        if self.__operation_stack.is_empty():
            print("No operations to undo")
            return None

        op_type, pid = self.__operation_stack.pop()
        patient = self.__patient_bst.search(pid)
        if not patient:
            print("Patient information corresponding to the operation does not exist")
            return None
        # Undo registration/calling
        if op_type == "register":
            self.__all_patients = [p for p in self.__all_patients if p.get_pid() != pid]
            patient.set_status("cancelled")
            print(f"Registration undone successfully | Patient ID:{pid}")
        elif op_type == "call":
            patient.set_status("waiting")
            self.__normal_queue.enqueue(patient)
            print(f"Calling undone successfully | Patient ID:{pid}")
        return (op_type, pid)

    def search_patient(self, pid):
        patient = self.__patient_bst.search(pid)
        if patient:
            print(f"Patient found successfully | {patient}")
            return patient
        else:
            print(f"Patient search failed | No patient with ID {pid}")
            return None

    def sort_patients(self, sort_type):
        if not self.__all_patients:
            print("No registered patients, cannot sort")
            return []

        sorted_patients = self.__all_patients.copy()
        if sort_type == "age":
            sorted_patients = PatientSorter.bubble_sort_by_age(sorted_patients)
        elif sort_type == "pid":
            sorted_patients = PatientSorter.selection_sort_by_pid(sorted_patients)
        elif sort_type == "name":
            sorted_patients = PatientSorter.merge_sort_by_name(sorted_patients)
        else:
            print("Unsupported sort type, supported types: age/pid/name")
            return []

        print(f"Sorting by {sort_type} completed, results are as follows:")
        for p in sorted_patients:
            print(p)
        return sorted_patients

    def get_visit_history(self):
        print("Patient visit history:")
        self.__visit_history.traverse()