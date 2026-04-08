from person import Person

class Patient(Person):
    # Patient class inheriting from Person, demonstrating inheritance
    _counter = 10000      # class variable for auto-increment ID

    def __init__(self, name, age, department, is_emergency=False, priority=5):
        super().__init__(name, age)
        self.__patient_id = Patient._counter
        Patient._counter += 1
        self.__department = department
        self.__is_emergency = is_emergency
        self.__priority = priority          # 1 = most urgent, 5 = least urgent
        self.__visit_status = "waiting"     # waiting / treated / cancelled

    # Implementation of abstract method
    def get_info(self):
        return f"Patient[ID={self.__patient_id}, Name={self._name}, Age={self._age}]"

    # Specific getters
    def get_pid(self):
        return self.__patient_id

    def get_department(self):
        return self.__department

    def is_emergency(self):
        return self.__is_emergency

    def get_priority(self):
        return self.__priority

    def get_status(self):
        return self.__visit_status

    def set_status(self, status):
        self.__visit_status = status

    def __str__(self):
        return (f"ID:{self.__patient_id} | Name:{self._name} | Age:{self._age} | "
                f"Dept:{self.__department} | Emergency:{self.__is_emergency} | "
                f"Priority:{self.__priority} | Status:{self.__visit_status}")