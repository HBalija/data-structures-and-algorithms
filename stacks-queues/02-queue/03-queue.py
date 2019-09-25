#!/usr/bin/env python3

"""
First in first out.

<--  first -------- last  <--

Singly linked list implementation
"""


class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:

    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def __str__(self):
        """
        Display queue elements.

        Most left element is the first one to leave the queue.
        """
        if not self.size:
            return '[ ]'

        current = self.first
        items = '[ '
        while current.next:
            items += '{}, '.format(current.value)
            current = current.next
        items += '{} ]'.format(self.last.value)

        return items

    def push(self, val):
        """
        Add new element to the end of the queue.
        """
        node = Node(val)

        if not self.size:
            self.first = node
            self.last = node
        else:
            # set the new node to be the last element
            self.last.next = node
            self.last = node

        self.size += 1
        return self.size

    def pop(self):
        """
        Remove first node from the queue.
        """
        if not self.size:
            return None

        node = self.first
        if (self.last == self.first):
            self.last = None
        self.first = self.first.next  # set the new first element
        node.next = None  # clean the old first element reference in queue
        self.size -= 1
        return node.value


queue = Queue()

print(queue.size)
print('-----------------')
print(queue.push('Hey'))
print(queue.push('there'))
print(queue.push('queue'))
print('first: ', queue.first.value)
print('last: ', queue.last.value)
print(queue.size)
print(queue)
print(queue.pop())
print('first: ', queue.first.value)
print('last: ', queue.last.value)
print(queue.size)
print(queue)
print(queue.pop())
print('first: ', queue.first.value)
print('last: ', queue.last.value)
print(queue.size)
print(queue)
print(queue.pop())
print(queue.size)
print(queue)
