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
        Check if passed value is in the tree.
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

    @property
    def bfs(self):
        """
        Return tree values using breadth-first search.

        Use list as a queue (O(n)time).
        """
        queue = []
        values = []
        dequeued = None

        queue.append(self.root)

        while len(queue):
            dequeued = queue.pop(0)
            values.append(dequeued.value)
            dequeued.left and queue.append(dequeued.left)
            dequeued.right and queue.append(dequeued.right)

        return values

    @property
    def dfs_preorder(self):
        """
        Return tree values using depth-first preOrder search.
        """
        values = []

        def traverse(node):
            values.append(node.value)
            node.left and traverse(node.left)
            node.right and traverse(node.right)

        traverse(self.root)
        return values

    @property
    def dfs_postorder(self):
        """
        Return tree values using depth-first postOrder search.
        """
        values = []

        def traverse(node):
            node.left and traverse(node.left)
            node.right and traverse(node.right)
            values.append(node.value)

        traverse(self.root)
        return values

    @property
    def dfs_in_order(self):
        """
        Return tree values using depth-first inOrder search.
        """
        values = []

        def traverse(node):
            node.left and traverse(node.left)
            values.append(node.value)
            node.right and traverse(node.right)

        traverse(self.root)
        return values


tree = BinarySearchTree()

tree.insert(10)
tree.insert(5)
tree.insert(13)
tree.insert(11)
tree.insert(2)
tree.insert(16)
tree.insert(7)
tree.insert(7)


"""
tree representation

                  10
          5                 13
      2       7         11      16

"""

print(tree.bfs)  # [10, 5, 13, 2, 7, 11, 16]
print(tree.dfs_preorder)  # [10, 5, 2, 7, 13, 11, 16]
print(tree.dfs_postorder)  # [2, 7, 5, 11, 16, 13, 10]
print(tree.dfs_in_order)  # [2, 5, 7, 10, 11, 13, 16]
