# Class representing a dynamic Array
class Array:
    # Constructor to initialize an empty array
    def __init__(self):
        self.data = []  # Data is stored in a list

    # Insert a value at a specific index in the array
    def insert(self, index, value):
        self.data.insert(index, value)

    # Delete the element at a specific index
    def delete(self, index):
        if index < len(self.data):  # Ensure the index is valid
            self.data.pop(index)

    # Access the element at a specific index
    def access(self, index):
        if index < len(self.data):  # Ensure the index is valid
            return self.data[index]
        return None  # Return None if index is out of bounds


# Class representing a Matrix (2D array)
class Matrix:
    # Constructor to initialize a matrix of given rows and columns with a default value
    def __init__(self, rows, cols, default=0):
        self.data = [[default for _ in range(cols)] for _ in range(rows)]  # Create a 2D list

    # Insert a value at a specific row and column in the matrix
    def insert(self, row, col, value):
        self.data[row][col] = value

    # Access the value at a specific row and column
    def access(self, row, col):
        return self.data[row][col]

    # Delete the value at a specific row and column (set to None)
    def delete(self, row, col):
        self.data[row][col] = None


# Class representing a Stack (LIFO - Last In First Out)
class Stack:
    # Constructor to initialize an empty stack
    def __init__(self):
        self.data = []  # Stack is implemented using a list

    # Push a value onto the stack
    def push(self, value):
        self.data.append(value)

    # Pop the value from the stack (remove and return the top element)
    def pop(self):
        if not self.is_empty():  # Check if the stack is not empty
            return self.data.pop()

    # Peek at the top value of the stack (without removing it)
    def peek(self):
        if not self.is_empty():  # Check if the stack is not empty
            return self.data[-1]

    # Check if the stack is empty
    def is_empty(self):
        return len(self.data) == 0


# Class representing a Queue (FIFO - First In First Out)
class Queue:
    # Constructor to initialize an empty queue
    def __init__(self):
        self.data = []  # Queue is implemented using a list

    # Enqueue a value to the end of the queue
    def enqueue(self, value):
        self.data.append(value)

    # Dequeue a value from the front of the queue (remove and return)
    def dequeue(self):
        if not self.is_empty():  # Check if the queue is not empty
            return self.data.pop(0)

    # Peek at the front value of the queue (without removing it)
    def peek(self):
        if not self.is_empty():  # Check if the queue is not empty
            return self.data[0]

    # Check if the queue is empty
    def is_empty(self):
        return len(self.data) == 0


# Class representing a Node for the Singly Linked List
class Node:
    # Constructor to initialize a node with a value and a next pointer
    def __init__(self, value):
        self.value = value  # Value of the node
        self.next = None  # Pointer to the next node (initialized to None)


# Class representing a Singly Linked List
class SinglyLinkedList:
    # Constructor to initialize an empty linked list
    def __init__(self):
        self.head = None  # The head pointer is initially set to None

    # Insert a new node with a given value at the beginning of the list
    def insert(self, value):
        new_node = Node(value)  # Create a new node
        new_node.next = self.head  # Point new node's next to the current head
        self.head = new_node  # Update head to point to the new node

    # Delete the first occurrence of a node with the given value
    def delete(self, value):
        current = self.head
        prev = None
        while current:  # Traverse the list
            if current.value == value:
                if prev:  # If the node to delete is not the first node
                    prev.next = current.next
                else:  # If the node to delete is the first node (head)
                    self.head = current.next
                return
            prev = current  # Move prev to current node
            current = current.next  # Move to the next node

    # Traverse the list and return the values of all nodes
    def traverse(self):
        current = self.head
        elements = []  # List to store node values
        while current:  # Traverse through the linked list
            elements.append(current.value)  # Add the value to elements list
            current = current.next  # Move to the next node
        return elements  # Return the list of node values


# Class representing a Node for a Tree (TreeNode with children)
class TreeNode:
    # Constructor to initialize a tree node with a value and a list of children
    def __init__(self, value):
        self.value = value  # Value of the node
        self.children = []  # List to store children nodes

    # Add a child node to the current node
    def add_child(self, child):
        self.children.append(child)

    # Traverse the tree starting from the current node and return all values
    def traverse(self):
        elements = [self.value]  # Start with the current node's value
        for child in self.children:  # Traverse through each child
            elements.extend(child.traverse())  # Add child's values by recursive traversal
        return elements  # Return the combined list of values from the node and its descendants
