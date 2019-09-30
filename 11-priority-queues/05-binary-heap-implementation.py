#!/usr/bin/env python3

"""
Min binary heap implementation

Insertion - O(log N)
Removal - O(log N)
Search - O(N)
"""


class Node:
    def __init__(self, val, priority):
        self.val = val
        self.priority = priority


class PriorityQueue:

    def __init__(self):
        self.values = []

    def __str__(self):
        return str([(item.val, item.priority) for item in self.values])

    def enqueue(self, val, priority):
        new_node = Node(val, priority)
        self.values.append(new_node)
        self.bubble_up()

    def bubble_up(self):
        idx = len(self.values) - 1
        element = self.values[idx]
        while idx > 0:
            parent_idx = (idx - 1) // 2
            parent = self.values[parent_idx]
            if element.priority >= parent.priority:
                break
            self.values[parent_idx] = element
            self.values[idx] = parent
            idx = parent_idx

    def dequeue(self):
        start = self.values[0]
        end = self.values.pop()
        if len(self.values) > 0:
            self.values[0] = end
            self.sink_down()
        return start

    def sink_down(self):
        idx = 0
        length = len(self.values)
        element = self.values[0]
        while True:
            left_child_idx = 2 * idx + 1
            right_child_idx = 2 * idx + 2
            left_child = None
            right_child = None
            swap = None

            if left_child_idx < length:
                left_child = self.values[left_child_idx]
                if left_child.priority < element.priority:
                    swap = left_child_idx
            if right_child_idx < length:
                right_child = self.values[right_child_idx]
                if ((not swap and right_child.priority < element.priority) or
                        (swap and right_child.priority < left_child.priority)):
                    swap = right_child_idx
            if (not swap):
                break
            self.values[idx] = self.values[swap]
            self.values[swap] = element
            idx = swap


ER = PriorityQueue()
ER.enqueue('common cold', 5)
ER.enqueue('gunshot wound', 1)
ER.enqueue('high fever', 4)
ER.enqueue('broken arm', 2)
ER.enqueue('glass in foot', 3)

print(ER)

"""
[
    ('gunshot wound', 1),
    ('broken arm', 2),
    ('high fever', 4),
    ('common cold', 5),
    ('glass in foot', 3)
]
"""

ER.dequeue()

print(ER)

"""
[
    ('broken arm', 2),
    ('glass in foot', 3),
    ('high fever', 4),
    ('common cold', 5)
]
"""
