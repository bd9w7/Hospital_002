# Intelligent Hospital Registration and Calling System

## Project Information
- Course: COMP2090SEF
- Group Members: LI Xuanyi (13640692), FAN Lingwen (13651866), HE Zhixun (13568063)
- Submission Date: April 12, 2026

## Project Structure
- `Task1_OOP/`: OOP-based Hospital Management System, including GUI and core business logic
- `Task2_SelfStudy/`: Self-study of data structures and algorithms (Min-Heap, Cocktail Sort) and corresponding tests

## Running Guide
1. Ensure Python 3.x environment is installed
2. Navigate to the `Task1_OOP/` directory and execute `python main.py`
3. After the GUI launches, you can perform operations such as registration, calling, revocation, search, and sorting
4. Test the self-study section: Navigate to `Task2_SelfStudy/` and execute `python test.py`

## Core Features
- Patient Registration (supports emergency/regular types with priority levels 1~5)
- Intelligent Calling: Emergency patients are prioritized based on Min-Heap, while regular patients are managed in a queue
- Operation Revocation: Supports undoing registration and calling operations (implemented with Stack + BST deletion + Heap/Queue recovery)
- Patient Search: Fast PID-based lookup using BST (Binary Search Tree)
- Multi-dimensional Sorting: By age (Bubble Sort), PID (Selection Sort), name (Merge Sort), priority (Cocktail Sort)
- Medical Visit History Records (Linked List)
- User-friendly Tkinter GUI

## OOP Concept Implementation
- Encapsulation: All attributes are private, with getter/setter methods provided
- Inheritance: `Patient` class inherits from the abstract base class `Person`
- Polymorphism: Abstract `Sorter` class with a unified `sort()` interface implemented by different sorting algorithms
- Abstraction: The `Person` class contains the abstract method `get_info()`

## Self-study Section
- Min-Heap: Used for the emergency patient priority queue with a time complexity of O(log n)
- Cocktail Sort: Bidirectional Bubble Sort, applied to sorting patients by priority

## Demonstration Video
[Click to watch the 5-minute demonstration video](https://your-video-link.com)

## Citation Declaration
This project is original and no external code was used. The GUI is implemented using Python's standard library tkinter.