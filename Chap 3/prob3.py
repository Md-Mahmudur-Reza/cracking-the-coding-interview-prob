"""
Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
threshold. Jmolement a data structure SetOfStacks that mimics this. seto-fstacks should be
composed of severa\ stacks and shou\d create a new stack once the prev·1ous one exceeds capacity.
Set0fStacks .push() and Set0fStacks. pop() should behave identically to a single stack
(that is, pop () should return the same values as it would if there were just a single stack).
FOLLOW UP
Implement a function popAt ( int index) which performs a pop operation on a specific sub-stack.
"""


class SetOfStack:
    def __init__(self):
        self.items = [[]]
        self.position = 0
        self.MAXLENGTH = 5

    def push(self, item):
        if len(self.items[self.position]) == self.MAXLENGTH:
            self.position += 1
            self.items.append([])
        self.items[self.position].append(item)

    def pop(self):
        if len(self.items[self.position]) == 0:
            self.items.pop()
            if self.position == 0:
                raise IndexError("Stack empty")
            else:
                self.position -= 1
        self.items[self.position].pop()

    def popAt(self, index):
        self.items[index].pop()

    def display(self):
        print(self.items)


if __name__ == "__main__":
    s = SetOfStack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    s.push(6)
    s.push(7)
    s.push(8)
    s.push(9)
    s.push(10)
    s.push(11)
    s.push(12)
    s.push(13)
    s.push(14)
    s.push(15)
    s.push(16)
    s.push(17)
    s.push(18)
    s.push(19)
    s.push(20)
    s.push(21)
    s.push(22)
    s.display()
    s.pop()
    s.pop()
    s.pop()
    s.display()
    s.push(31)
    s.push(32)
    s.push(33)
    s.push(34)
    s.display()
    s.pop()
    s.pop()
    s.pop()
    s.pop()
    s.display()
    s.popAt(2)
    s.display()
