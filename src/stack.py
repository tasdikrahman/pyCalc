"""
Stack class implementation for the input taken from the user by buttons

attributes: 
methods:
"""

class Stack():
    def __init__(self):
        self.container = []

    def isEmpty(self):
        return self.container.size() == 0

    def insert(self, data):
        self.container.append(data)

    def undo(self):
        self.container.pop()

    def size(self):
        return self.container.size()