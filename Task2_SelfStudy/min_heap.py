# MinHeap Implementation
# Data Structure: Complete Binary Tree
class MinHeap:
    def __init__(self):
        self.heap = [] # Heap list

    # Insert element
    def push(self, val):
        self.heap.append(val)
        self._up(len(self.heap) - 1)

    # Heapify up
    def _up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i] < self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break

    # Pop minimum
    def pop(self):
        if not self.heap:
            return None # Handle empty heap
        min_val = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self._down(0)
        return min_val

    # Heapify down
    def _down(self, i):
        size = len(self.heap)
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i
            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest == i:
                break
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest
