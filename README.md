# Smart Hospital Registration and Call System

## Project Information
- Course: COMP2090SEF
- Team Members: Li Xuanyi (13640692), Fan Lingwen (13651866), He Zhixun (13568063)
- Submission Date: April 12, 2026

## Project Structure
This project is divided into two major modules, each corresponding to the course assignment requirements:
- `Task1_OOP/`: Object-oriented implementation of a hospital registration, queuing, and call-up system, including a complete GUI and business logic
- `Task2_SelfStudy/`: Self-study content, including the implementation and testing of min-heap and cocktail sort

## How to Run
1. Ensure Python 3.x is installed
2. Entry point: Run `main.py` in the `Task1_OOP/` directory
3. Run self-study module tests: Execute `test_cases.py` in the `Task2_SelfStudy/` directory

## Core Features
- Patient Registration: Divided into general and emergency appointments; priority levels 1–5 can be set
- Intelligent Call System: Implements emergency priority using a min-heap; general patients are managed via a queue
- Undo Functionality: Implements undo of the most recent operation using a stack
- Quick Search: Implements fast patient ID lookup using a binary search tree
- Multi-dimensional Sorting: Supports sorting by multiple criteria such as age, ID, name, and priority
- Medical Record Management: Uses linked lists to maintain medical history
- Graphical Interface: Implements a simple and user-friendly GUI using Tkinter

## Object-Oriented Programming (OOP)
- Encapsulation: Private class attributes with safe access via getters/setters
- Inheritance: The `Patient` class inherits from `Person`
- Polymorphism: The sorting module enables quick replacement of various sorting algorithms through a unified interface
- Abstraction: Base classes define abstract methods, while subclasses provide concrete implementations

## Self-Study Content
- Min-Heap: Used to implement priority levels for emergency patients
- Cocktail Sort: A bidirectional bubble sort suitable for partially sorted datasets

## Disclaimer
This project is an original course assignment and does not directly reference external source code.
The GUI was developed using Python’s built-in tkinter library.