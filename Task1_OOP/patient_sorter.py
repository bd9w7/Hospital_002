from abc import ABC, abstractmethod

# Abstract sorter (polymorphism)
class Sorter(ABC):
    @abstractmethod
    def sort(self, patients):
        pass

class BubbleSortByAge(Sorter):
    def sort(self, patients):
        n = len(patients)
        for i in range(n):
            for j in range(0, n-i-1):
                if patients[j].get_age() > patients[j+1].get_age():
                    patients[j], patients[j+1] = patients[j+1], patients[j]
        return patients

class SelectionSortByPid(Sorter):
    def sort(self, patients):
        n = len(patients)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if patients[j].get_pid() < patients[min_idx].get_pid():
                    min_idx = j
            patients[i], patients[min_idx] = patients[min_idx], patients[i]
        return patients

class MergeSortByName(Sorter):
    def sort(self, patients):
        if len(patients) <= 1:
            return patients
        mid = len(patients) // 2
        left = self.sort(patients[:mid])
        right = self.sort(patients[mid:])
        return self._merge(left, right)

    def _merge(self, left, right):
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

# Patient sorter (unified entry, demonstrating polymorphism)
class PatientSorter:
    def __init__(self):
        self.bubble_sorter = BubbleSortByAge()
        self.selection_sorter = SelectionSortByPid()
        self.merge_sorter = MergeSortByName()

    def bubble_sort_by_age(self, patients):
        return self.bubble_sorter.sort(patients)

    def selection_sort_by_pid(self, patients):
        return self.selection_sorter.sort(patients)

    def merge_sort_by_name(self, patients):
        return self.merge_sorter.sort(patients)