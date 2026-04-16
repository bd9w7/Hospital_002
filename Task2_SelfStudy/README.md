# Self-study module: minimum pile and cocktail sorting

## Module content

This module is an independent learning task of the course, which realizes the minimum heap and cocktail sorting, and provides test case verification function correctness.

## Demonstration video
[Task2_video](https://drive.google.com/file/d/1vBMv57vKvDrNMvsIDwtNctTG_I-9RMGU/view?usp=sharing)

## Document description

- `min_heap.py`: the minimum heap is fully implemented, including insertion, ejection, stacking and other core operations

- `cocktail_sort.py`: cocktail sorting implementation, support custom sorting keys

- `test_cases.py`: unit test, verify the correctness of heap and sorting algorithms

- `User_Guide.md`: Instructions for use and operation

## Learning content

### Minimum Heap (MinHeap)

- Structure: complete binary tree

- Core operation: insert, extract the top of the heap, up/down heap

- Application Scenario: Hospital Emergency Patient Priority Cohort

### Cocktail Sort (Cocktail Sort)

- Principle: two-way bubbling sorting, left and right alternate traversal and exchange

- Features: More efficient for approximate ordered arrays

- Application scenario: the list of patients is sorted by priority, age and other dimensions