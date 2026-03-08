class MinHeap:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.heap[0]

    def insert(self, item):
        self.heap.append(item)
        self._bubble_up(len(self.heap) - 1)

    def _bubble_up(self, idx):

        while idx > 0:
            parent_idx = (idx - 1) // 2

            if self.heap[idx] < self.heap[parent_idx]:
                self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
                idx = parent_idx
            else:
                break

    def pop(self):
        if self.is_empty():
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        top = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._bubble_down(0)
        return top

    def _bubble_down(self, idx):
        n = len(self.heap)
        while True:
            left_idx = 2 * idx + 1
            right_idx = 2 * idx + 2
            min_idx = idx


            if left_idx < n and self.heap[left_idx] < self.heap[min_idx]:
                min_idx = left_idx

            if right_idx < n and self.heap[right_idx] < self.heap[min_idx]:
                min_idx = right_idx

            if min_idx != idx:
                self.heap[idx], self.heap[min_idx] = self.heap[min_idx], self.heap[idx]
                idx = min_idx
            else:
                break

    def traverse(self):
        if self.is_empty():
            print("Heap is empty")
            return
        print("Min-heap elements: ", self.heap)