#!/usr/bin/env python3


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def push(self, val):
        """
        Add item to the end of the list.
        """
        node = Node(val)

        if not self.length:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node
        self.length += 1

        return self

    def pop(self):
        """
        Remove an item from the end of the list.
        """
        if not self.length:
            return None

        new_tail = self.head
        tail = self.tail

        while new_tail.next and new_tail.next != tail:
            new_tail = new_tail.next

        new_tail.next = None
        self.tail = new_tail
        self.length -= 1

        if not self.length:
            self.head = None
            self.tail = None

        return tail

    def shift(self):
        """
        Remove item from beginning of the list.
        """
        if not self.length:
            return None

        old_head = self.head
        self.head = old_head.next
        self.length -= 1

        if not self.length:
            self.tail = None

        return old_head

    def unshift(self, val):
        """
        Add item to beginning of the list.
        """
        node = Node(val)

        if not self.length:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

        self.length += 1

        return self

    def get(self, idx):
        """
        Get an item from the list based on item index.
        """
        if idx < 0 or idx >= self.length:
            return None

        element = self.head
        counter = 0

        while counter < idx:
            element = element.next
            counter += 1

        return element

    def set(self, idx, value):
        """
        Set a new value for existing item based on index.
        """
        node = self.get(idx)
        if not node:
            return False
        node.val = value
        return True

    def insert(self, idx, value):
        """
        Insert a new value between existing items based on position.
        """
        if idx < 0 or idx > self.length:
            return False

        if idx == self.length:
            self.push(value)
        elif idx == 0:
            self.unshift(value)
        else:
            node_before = self.get(idx - 1)
            node_after = node_before.next

            new_node = Node(value)
            node_before.next = new_node
            new_node.next = node_after
            self.length += 1

        return True

    def remove(self, idx):
        """
        Remove a value by its index.
        """
        if idx < 0 or idx >= self.length:
            return None

        if idx == self.length - 1:
            return self.pop()
        if idx == 0:
            return self.shift()

        node_before = self.get(idx - 1)
        node = node_before.next
        node_before.next = node.next
        self.length -= 1

        return node

    def reverse(self):
        """
        Reverse the order of items in list
        """
        node = self.head
        self.head = self.tail
        self.tail = node

        _prev = None
        _next = None

        for i in range(self.length):
            _next = node.next
            node.next = _prev
            _prev = node
            node = _next

        return self

    def __str__(self):
        if not self.length:
            return "[ ]"

        current = self.head
        items = "[ "
        while current.next:
            items += "{}, ".format(current.val)
            current = current.next
        items += "{} ]".format(self.tail.val)

        return items
