from abc import ABC, abstractmethod

class Person(ABC):
    # Abstract base class demonstrating abstraction
    def __init__(self, name, age):
        self._name = name          # protected attribute
        self._age = age

    @abstractmethod
    def get_info(self):
        # Abstract method, to be implemented by subclasses---polymorphism
        pass

    # Getters (encapsulation)
    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        self._age = age