# Intelligent Hospital Appointment and Queuing System

## Project Information
The hospital intelligent appointment and queueing system is developed based on object-oriented Python. It solves the practical problem of patients waiting in line for medical treatment in hospitals, realizes the core functions of emergency priority and intelligent queuing, and ensures patients can receive orderly medical treatment.  

### Group Information
- Course:
    COMP2090SEF
- Group members：
    LI Xuanyi 13640692
    FAN Lingwen 13651866
    HE Zhixun 13568063

## content introduction
### Directory structure
- Task1_OOP：
    main.py               # GUI main program
    data_structures.py    # Classical data structure encapsulation
    patient_manager.py    # Sorting algorithm, data management
    appointment_system.py # Register, call...

#### TASK1 Core Function
1. Patient registration and information management
Supports the addition, modification, and deletion of patient basic information
2. Intelligent call number
Emergency patients are automatically inserted into the head of the queue for priority treatment, which solves the pain point that the priority of emergency treatment in outpatient clinics cannot be guaranteed.
3. Operate the revocation function
Based on the stack data structure, the rollback of the last 5 business operations is implemented, covering scenarios such as call number, information modification, and patient deletion, and reducing the impact of misoperation.
4. Quick search of patient information
Supports multi-dimensional precise or fuzzy search for name, visit number, and visit department, achieving millisecond-level result return and improving the work efficiency of medical staff.
5. Multi-dimensional patient ranking
Package multiple sorting algorithms, support or sorting according to visit number, age, disease grade, registration time..., and adapt to different management scenarios. 

#### TASK1 Application of OOP
- Encapsulation: Package all code related to business and data into "classes". Each class only exposes the necessary public interface to the outside world, and the internal core attributes and implementation logic are encapsulated in private form, prohibiting direct access from the outside.
- Inheritance: It avoids repetition of code and also enables code extension. You develop a basic data structure class. Next, you develop subclasses to business operations such as Registration or Call Number. The specific scenarios will allow you to modify the standard approaches.
- Polymorphism: The sorting function operates similarly regardless of how you wish to sort the data - disease grade, age, visit number and order, etc. A comparable method is used. The actual sorting is handled by different sorting classes, so that one interface offers many types of sorting and the code is simpler to change and expand.
- Abstraction: The complex code is concealed and you are left with simple and clear things to work with.

## Technology Stack
- Development Language: Python 3.x
- GUI Framework: tkinter (Python standard library, provides native graphical interface)
- Core Technologies:
  - Object-Oriented Programming：Encapsulation/Inheritance/Polymorphism/Abstraction
  - Classic Data Structures：LinkedList, Stack, Queue, Binary Search Tree
  - Sorting Algorithms：Bubble Sort, Selection Sort, Merge Sort, Cocktail Sort
  - Self-Studied Data Structures：MinHeap for priority queue optimization