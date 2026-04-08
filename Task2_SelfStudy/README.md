# Task2：Self-Study of Data Structures and Algorithms  (Min-Heap and Cocktail Sort)
## Directory structure
Task2_SelfStudy：
    min_heap.py: Complete implementation of Min-Heap, including core ADT methods
    cocktail_sort.py: Complete implementation of Cocktail Sort, supporting multi-dimensional sorting
    test_cases.py: test cases
    User_Guide.md: Running and usage guide

## Content Introduction
This module is interoperable with the hospital calling system in Task1 and implements emergency priority:
- min_heap.py: Complete MinHeap implementation (ADT)
- cocktail_sort.py: Cocktail sort implementation with optional key function
- test.py: Unit tests for both

## Self-Study Content
### MinHeap
1. ADT: Binary tree structure supporting core operations such as insertion, popping the heap top, and heapification
2. Core Application: Priority queue for emergency patients in hospitals (priority 1 for first consultation)

### Cocktail Sort
1. Algorithm Type: Bidirectional bubble sort, traversing and swapping bidirectionally from left to right, right to left
2. Core Application: Bidirectional sorting of hospital patients by priority/age/ID, optimizing sorting efficiency for partially ordered data
