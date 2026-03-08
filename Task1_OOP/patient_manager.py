# Patient Management Module
import random

class Patient:
    def __init__(self, name, age, department, is_emergency=False, priority=5):
        self.__patient_id = random.randint(10000, 99999)  # Unique patient ID
        self.__name = name  # Name
        self.__age = age  # Age
        self.__department = department  # Department
        self.__is_emergency = is_emergency  # Is emergency
        self.__priority = priority  # Priority (1 = most urgent)
        self.__visit_status = "waiting"  # Visit status (waiting/treated/finished)

    # Getter methods
    def get_pid(self):
        return self.__patient_id

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_department(self):
        return self.__department

    def is_emergency(self):
        return self.__is_emergency

    def get_priority(self):
        return self.__priority

    def set_status(self, status):
        self.__visit_status = status

    def get_status(self):
        return self.__visit_status

    def __str__(self):
        return f"ID:{self.__patient_id} | Name:{self.__name} | Age:{self.__age} | Department:{self.__department} | Emergency:{self.__is_emergency} | Priority:{self.__priority} | Status:{self.__visit_status}"

class PatientSorter:
    @staticmethod
    def bubble_sort_by_age(patients):
        n = len(patients)
        for i in range(n):
            for j in range(0, n-i-1):
                if patients[j].get_age() > patients[j+1].get_age():
                    patients[j], patients[j+1] = patients[j+1], patients[j]
        return patients

    @staticmethod
    def selection_sort_by_pid(patients):
        n = len(patients)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if patients[j].get_pid() < patients[min_idx].get_pid():
                    min_idx = j
            patients[i], patients[min_idx] = patients[min_idx], patients[i]
        return patients

    @staticmethod
    def merge_sort_by_name(patients):
        if len(patients) <= 1:
            return patients
        mid = len(patients) // 2
        left = PatientSorter.merge_sort_by_name(patients[:mid])
        right = PatientSorter.merge_sort_by_name(patients[mid:])
        return PatientSorter._merge(left, right)

    @staticmethod
    def _merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i].get_name() < right[j].get_name():
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result