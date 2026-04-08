# LinkedList (for visit history)
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
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return result

# Stack (for undo operations)
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if self.items else None

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        return self.items[-1] if self.items else None

# Queue (for normal patients)
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft() if self.items else None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Binary Search Tree (for PID-based quick search)
class BSTNode:
    def __init__(self, key, data):
        self.key = key
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

    def delete(self, key):
        self.root = self._delete_rec(self.root, key)

    def _delete_rec(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete_rec(node.left, key)
        elif key > node.key:
            node.right = self._delete_rec(node.right, key)
        else:
            # Node to be deleted found
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # Node with two children: find the smallest node in the right subtree
            min_node = self._find_min(node.right)
            node.key = min_node.key
            node.data = min_node.data
            node.right = self._delete_rec(node.right, min_node.key)
        return node

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node