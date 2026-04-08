from data_structures import Stack, Queue, BinarySearchTree, LinkedList
from patient import Patient
from patient_sorter import PatientSorter
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Task2_SelfStudy.min_heap import MinHeap
from Task2_SelfStudy.cocktail_sort import cocktail_sort

class AppointmentSystem:
    """Core hospital appointment and calling system, integrating all data structures and algorithms"""
    def __init__(self):
        self.__operation_stack = Stack()
        self.__normal_queue = Queue()
        self.__patient_bst = BinarySearchTree()
        self.__visit_history = LinkedList()
        self.__all_patients = []
        self.__emergency_heap = MinHeap()
        self.__call_counter = 0          # for stable ordering in heap

    def register_patient(self, name, age, department, is_emergency=False, priority=5):
        patient = Patient(name, age, department, is_emergency, priority)
        self.__patient_bst.insert(patient.get_pid(), patient)
        if is_emergency:
            # Store tuple (priority, sequence_number, patient) in heap
            self.__emergency_heap.insert((patient.get_priority(), self.__call_counter, patient))
            self.__call_counter += 1
        else:
            self.__normal_queue.enqueue(patient)
        self.__all_patients.append(patient)
        self.__operation_stack.push(("register", patient.get_pid()))
        return patient.get_pid()

    def call_patient(self):
        # Priority: emergency heap first
        if not self.__emergency_heap.is_empty():
            _, _, patient = self.__emergency_heap.pop()
            patient.set_status("treated")
            self.__operation_stack.push(("call", patient.get_pid()))
            self.__visit_history.add_at_end(patient)
            return patient
        # Then normal queue
        if not self.__normal_queue.is_empty():
            patient = self.__normal_queue.dequeue()
            patient.set_status("treated")
            self.__operation_stack.push(("call", patient.get_pid()))
            self.__visit_history.add_at_end(patient)
            return patient
        return None

    def undo_operation(self):
        if self.__operation_stack.is_empty():
            return None
        op_type, pid = self.__operation_stack.pop()
        patient = self.__patient_bst.search(pid)
        if not patient:
            return None
        if op_type == "register":
            self.__patient_bst.delete(pid)
            self.__all_patients = [p for p in self.__all_patients if p.get_pid() != pid]
            patient.set_status("cancelled")
        elif op_type == "call":
            patient.set_status("waiting")
            if patient.is_emergency():
                self.__emergency_heap.insert((patient.get_priority(), self.__call_counter, patient))
                self.__call_counter += 1
            else:
                self.__normal_queue.enqueue(patient)
        return (op_type, pid)

    def search_patient(self, pid):
        patient = self.__patient_bst.search(pid)
        return patient if patient else None

    def sort_patients(self, sort_type):
        if not self.__all_patients:
            return []
        sorted_patients = self.__all_patients.copy()
        sorter = PatientSorter()
        if sort_type == "age":
            sorted_patients = sorter.bubble_sort_by_age(sorted_patients)
        elif sort_type == "pid":
            sorted_patients = sorter.selection_sort_by_pid(sorted_patients)
        elif sort_type == "name":
            sorted_patients = sorter.merge_sort_by_name(sorted_patients)
        elif sort_type == "priority_cocktail":
            sorted_patients = cocktail_sort(sorted_patients, key=lambda p: p.get_priority())
        else:
            raise ValueError("Unsupported sort type")
        return sorted_patients

    def get_visit_history(self):
        return self.__visit_history.traverse()

    def get_all_patients(self):
        return self.__all_patients.copy()