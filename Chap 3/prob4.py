"""
Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.
"""


class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, item):
        self.stack1.append(item)

    def pop(self):
        if len(self.stack2) == 0:
            while len(self.stack1) != 0:
                poped_item = self.stack1.pop()
                self.stack2.append(poped_item)
        item = self.stack2.pop()
        print(f"{item} poped")

    def peek(self):
        if len(self.stack2) == 0:
            while len(self.stack1) != 0:
                poped_item = self.stack1.pop()
                self.stack2.append(poped_item)
        print(f"top item : {self.stack2[-1]}")


if __name__ == "__main__":
    q = MyQueue()
    q.push(10)
    q.push(9)
    q.pop()
    q.peek()
    q.push(8)
    q.peek()
