#!/usr/bin/env python3


class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:

    vlaues = []

    def __init__(self):
        self.root = None

    def insert(self, value):
        """
        Add a new value to proper position in BST.
        """
        node = Node(value)

        if not self.root:
            self.root = node
            return self

        current = self.root

        while True:
            if value == current.value:
                return None

            if value < current.value:
                if not current.left:
                    current.left = node
                    return self
                #  move to the next left
                current = current.left

            elif value > current.value:
                if not current.right:
                    current.right = node
                    return self
                #  move to the next right
                current = current.right

    def contains(self, value):
        """
        Return boolean value depending on passed value.
        """
        if not self.root:
            return False

        current = self.root

        while current:
            if value == current.value:
                return True

            if value < current.value:
                current = current.left  # move to the next left
            elif value > current.value:
                current = current.right  # move to the next right
        return False


tree = BinarySearchTree()

tree.insert(10)
tree.insert(5)
tree.insert(13)
tree.insert(11)
tree.insert(2)
tree.insert(16)
tree.insert(7)
tree.insert(7)

print(tree.contains(10))  # True
print(tree.contains(100))  # False
print(tree.contains(2))  # True
print(tree.contains(17))  # False
