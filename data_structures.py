# data_structures.py - Contains the implementations of basic data structures

class Array:
    def __init__(self, data=None):
        self.data = data or []

    def __repr__(self):
        return f"Array({self.data})"

    def append(self, value):
        self.data.append(value)

    def remove(self, value):
        self.data.remove(value)


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return f"LinkedList({elements})"

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node


class Stack:
    def __init__(self):
        self.items = []

    def __repr__(self):
        return f"Stack({self.items})"

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0


class Queue:
    def __init__(self):
        self.items = []

    def __repr__(self):
        return f"Queue({self.items})"

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty(self):
        return len(self.items) == 0
