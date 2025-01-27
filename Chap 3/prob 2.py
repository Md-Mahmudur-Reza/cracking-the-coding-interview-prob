"""
Stack Min: How would you design a stack which, in addition to push and pop, has a function min
which returns the minimum element? Push, pop and min should all operate in 0(1) time.
"""

class Stack:

    def __init__(self):
        self.items = []
        self.min_stack = []

    def push(self, item):
        self.items.append(item)
        print(f"pushed {item} to stack")
        if (len(self.min_stack) == 0):
            self.min_stack.append(item)
        elif (item <= self.min_stack[-1]):
            self.min_stack.append(item)
    
    def pop(self):
        if len(self.items) == 0:
            raise IndexError("Stack empty")
        else : 
            poped_item = self.items.pop()
            if (poped_item == self.min_stack[-1]):
                self.min_stack.pop()
    
    def min(self):
        if (len(self.min_stack)==0):
            print("no item")
        else:
            print(self.min_stack[-1])


if __name__ == "__main__":
    s = Stack()
    s.push(2)
    s.min()
    s.push(8)
    s.min()
    s.push(10)
    s.push(1)
    s.push(6)
    s.min()
    s.push(0)
    s.min()
    s.pop()
    s.min()