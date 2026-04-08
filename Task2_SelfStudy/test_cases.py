# Test Module
import time
from min_heap import MinHeap
from cocktail_sort import cocktail_sort

print("--SelfStudy Test--")

# Test MinHeap
print("\n1. MinHeap Test")
heap = MinHeap()
for num in [5, 3, 7, 1, 2]:
    heap.push(num)
print("Pop order:", [heap.pop() for _ in range(5)])

# Test sorting + time cost
print("\n2. Cocktail Sort Test")
arr = [8, 2, 6, 1, 3, 9, 4]
print("Original:", arr)
start = time.time()
sorted_arr = cocktail_sort(arr)
end = time.time()
print("Sorted:", sorted_arr)
print(f"Time: {end - start:.6f}s")

# Edge case test
print("\n3. Edge Case Test (Empty array)")
print("Empty array sorted:", cocktail_sort([]))
