# Intelligent hospital registration and queuing system (OOP implementation)

## Project Overview

Based on the Python object-oriented programming idea, this system realizes complete business processes such as hospital outpatient registration, queuing, calling, query and sorting, and focuses on solving practical problems such as emergency priority, efficient queuing and operation revocable.

## Basic information

- Course: COMP2090SEF

- Group members: Li Xuanyi, Fan Lingwen, He Zhixun

## Demonstration video

[Function Demonstration Video][(https://drive.google.com/file/d/1U4vtuItlU27Z4EdvAhI5DxUbWB6O-7nM/view?usp=sharing)]

## File structure

- `main.py`: system entrance, start the Tkinter graphical interface

- `person.py`: abstract base class `Person`, reflecting the characteristics of encapsulation and abstraction

- `patient.py`: patient class, inherited from `Person`

- `appointment.py`: core logic such as registration, call, cancellation, priority queue, etc.

- `data_structures.py`: basic data structure implementation (linked list, stack, queue, binary search tree)

- `patient_sorter.py`: polymorphic sorting module, encapsulates a variety of sorting algorithms

## Functional module

1. **Patient information management**

Support adding, modifying and deleting patient information, and recording the registration type and priority.

2. **Intelligent Calling System**

Emergency patients are given priority through the minimum stack, and ordinary patients follow the first-in-first-first-out rule.

3. **Operation cancellation**

Record the latest operation based on the stack structure, and support the rollback of registration, calling, modification and other operations.

4. **High-efficiency inquiry**

Based on the binary search tree, it realizes quick query according to PID to improve retrieval efficiency.

Five. **Multidimensional sorting**

Support sorting by medical number, age, disease priority, name and other dimensions, and use algorithms such as bubbling, selection, aggregation, cocktail sorting, etc.

6. **Medical record**

Use the linked list to store and manage the patient's visit history.

## Highlights of object-oriented design

- **Encapsulation**: Data and methods are encapsulated inside the class to provide a secure interface externally.

- **Inheritance**: Reuse code through base classes to enhance scalability

- **Molymorphism**: Unified sorting interface, different algorithms can be replaced freely

- **Abstract**: Hide the underlying implementation and simplify the upper-level call logic

## Technology Stack

- Language: Python 3.x

- Interface: Tkinter

- Data structure: linked list, stack, queue, binary search tree, heap

- Algorithm: a variety of classic sorting algorithms