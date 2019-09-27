#!/usr/bin/env python3

"""
Last in first out.

-->
<--   last ---------------------- first

Singly linked list implementation
"""


class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:

    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def __str__(self):
        """
        Display stack elements.

        Most left element is the first one to leave the stack.
        """
        if not self.size:
            return '[ ]'

        current = self.last
        items = '[ '
        while current.next:
            items += '{}, '.format(current.value)
            current = current.next
        items += '{} ]'.format(self.first.value)

        return items

    def push(self, val):
        """
        Add a new item to the top of the stack.
        """
        node = Node(val)

        if not self.size:
            self.first = node
            self.last = node
        else:
            # set the new node to be the last one entering the stack
            node.next = self.last
            self.last = node

        self.size += 1
        return self.size

    def pop(self):
        """
        Remove item from the top of the stack.
        """
        if not self.size:
            return None

        node = self.last  # last node entering the stack to be popped
        if (self.last == self.first):
            self.first = None

        self.last = node.next  # set the new last node
        node.next = None  # clean the reference from the popped node
        self.size -= 1
        return node.value


stack = Stack()

print(stack.size)
print('-----------------')
print(stack.push('Hey'))
print(stack.push('there'))
print(stack.push('stack'))
print('last: ', stack.last.value)
print('first: ', stack.first.value)
print(stack.size)
print(stack)
print(stack.pop())
print('last: ', stack.last.value)
print('first: ', stack.first.value)
print(stack.size)
print(stack)
print(stack.pop())
print('last: ', stack.last.value)
print('first: ', stack.first.value)
print(stack.size)
print(stack)
print(stack.pop())
print(stack.size)
print(stack)
