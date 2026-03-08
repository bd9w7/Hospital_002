class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty(self):
        return len(self.items) == 0

class BSTNode:
    def __init__(self, key, data):
        self.key = key  # Patient ID as search key
        self.data = data 
        self.left = None
        self.right = None

class BinarySearchTree: 
    def __init__(self):
        self.root = None

    def insert(self, key, data):
        self.root = self._insert_rec(self.root, key, data)

    def _insert_rec(self, node, key, data):
        if node is None:
            return BSTNode(key, data)
        if key < node.key:
            node.left = self._insert_rec(node.left, key, data)
        else:
            node.right = self._insert_rec(node.right, key, data)
        return node

    def search(self, key):
        return self._search_rec(self.root, key)

    def _search_rec(self, node, key):
        if node is None or node.key == key:
            return node.data if node else None
        if key < node.key:
            return self._search_rec(node.left, key)
        return self._search_rec(node.right, key)