"""
Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
an additional temporary stack, but you may not copy the elements into any other data structure
(such as an array). The stack supports the following operations: push, pop, peek, and is Empty.
"""


class Stack:
    def __init__(self):
        self.items = []
        self.temp_stack = []

    def push(self, item):
        while self.items and self.items[-1] > item:
            self.temp_stack.append(self.items.pop())

        self.items.append(item)

        while len(self.temp_stack):
            self.items.append(self.temp_stack.pop())

    def display(self):
        print(self.items)


if __name__ == "__main__":
    s = Stack()
    s.push(6)
    s.display()
    s.push(5)
    s.display()
    s.push(4)
    s.push(3)
    s.display()
    s.push(5)
    s.push(7)
    s.display()
