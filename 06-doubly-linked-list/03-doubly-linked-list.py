#!/usr/bin/env python3


class Node:

    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def push(self, val):
        """
        Add new item to the end of the list.
        """
        node = Node(val)

        if not self.length:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        self.length += 1
        return self

    def pop(self):
        """
        Remove last item from the list.
        """
        if not self.length:
            return None

        tail = self.tail

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = tail.prev
            self.tail.next = None
            tail.prev = None

        self.length -= 1
        return tail

    def shift(self):
        """
        Remove first item from the list.
        """
        if not self.length:
            return None

        head = self.head

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = head.next
            self.head.prev = None
            head.next = None

        self.length -= 1
        return head

    def unshift(self, val):
        """
        Add an item to the beginning of the list.
        """
        node = Node(val)

        if not self.length:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node

        self.length += 1
        return self

    def get(self, idx):
        """
        Get the item by its index.
        """
        if idx < 0 or idx >= self.length:
            return None

        element = None

        if idx <= self.length / 2:
            counter = 0
            element = self.head
            while counter < idx:
                element = element.next
                counter += 1
        else:
            counter = self.length - 1
            element = self.tail
            while counter > idx:
                element = element.prev
                counter -= 1

        return element

    def set(self, idx, val):
        """
        Set the new value for a index.
        """
        node = self.get(idx)
        if not node:
            return False

        node.value = val
        return True

    def insert(self, idx, val):
        """
        Insert new value on index position.
        """
        if idx < 0 or idx > self.length:
            return False

        if idx == 0:
            self.unshift(val)
        elif idx == self.length:
            self.push(val)
        else:
            node = Node(val)
            node_before = self.get(idx - 1)

            node_before.next.prev = node
            node.next = node_before.next

            node_before.next = node
            node.prev = node_before

            self.length += 1

        return True

    def remove(self, idx):
        """
        Remove item by index.
        """
        if idx < 0 or idx >= self.length:
            return None
        if idx == 0:
            return self.shift()
        if idx == self.length - 1:
            return self.pop()

        node = self.get(idx)

        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
        self.length -= 1
        return node

    def __str__(self):
        if not self.length:
            return "[ ]"

        current = self.head
        items = "[ "
        while current.next:
            items += "{}, ".format(current.value)
            current = current.next
        items += "{} ]".format(self.tail.value)

        return items


lst = DoublyLinkedList()

lst.push(":")
lst.push("Hello")
lst.push("there")

print(lst)
print("head:", lst.head.value)
print("tail: ", lst.tail.value)
print(lst.length)
print(lst.remove(1))
print(lst)
print("head:", lst.head.value)
print("tail: ", lst.tail.value)
print(lst.length)
