class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def search(self, target):
        if self.data == target:
            print("Found it")
            return self

        if self.left and self.data > target:
            return self.left.search(target)

        if self.right and self.data < target:
            return self.right.search(target)

        print("Value not found")

    def add(self, data):
        if self.data == data:
            return

        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.add(Node)

        if data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.add(data)

    def traverseInorder(self):
        if self.left:
            self.left.traverseInorder()
        print(self.data)
        if self.right:
            self.right.traverseInorder()


if __name__ == "__main__":
    ar = [1, 2, 3, 4, 5, 6, 7]

    node = Node(ar[0])

    for item in ar[1:]:
        node.add(item)

    node.traverseInorder()
