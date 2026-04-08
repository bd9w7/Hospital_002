import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Task2_SelfStudy.min_heap import MinHeap
from Task2_SelfStudy.cocktail_sort import cocktail_sort

# Test MinHeap
def test_min_heap():
    print("=== Testing MinHeap ===")
    heap = MinHeap()
    data = [5, 3, 8, 1, 4]
    for d in data:
        heap.insert(d)
    print("Heap after inserts:", heap.traverse())
    sorted_list = []
    while not heap.is_empty():
        sorted_list.append(heap.pop())
    print("Pop order (ascending):", sorted_list)
    assert sorted_list == sorted(data), "Heap sort error"

# Test Cocktail Sort
def test_cocktail_sort():
    print("\n=== Testing Cocktail Sort ===")
    arr = [5, 1, 4, 2, 8, 0, 3]
    sorted_arr = cocktail_sort(arr)
    print("Original array:", arr)
    print("Sorted array:", sorted_arr)
    assert sorted_arr == sorted(arr), "Cocktail sort error"

    # Test with custom key (string length)
    words = ["apple", "kiwi", "banana", "pear"]
    sorted_words = cocktail_sort(words, key=len)
    print("Sorted by length:", sorted_words)
    assert sorted_words == ["kiwi", "pear", "apple", "banana"], "Custom key error"

if __name__ == "__main__":
    test_min_heap()
    test_cocktail_sort()
    print("\n✅ All tests passed")