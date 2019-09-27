#!/usr/bin/env python3

"""

Write a function called is_same_improved, which accepts two lists.
The function should return true if every value in the list
has its corresponding value squared in the second
alistrray. The frequency of values must be the same.

same([1, 2, 3], [4, 1, 9]) // true
same([1, 2, 3], [1, 9]) // false
same([1, 2, 1], [4, 4, 1]) // false (must be same freqquency)

"""


def is_same(lst1, lst2):
    """
    Naive approach - O(n**2)
    """
    if len(lst1) != len(lst2):
        return False

    for item in lst1:
        # searching the index of list 2 with value of list 1 squared
        # index --> O(n)
        try:
            index = lst2.index(item**2)
        except ValueError:
            # is not in the list
            return False

        # remove element from list 2
        lst2.pop(index)

    return True


print('NAIVE')
print(is_same([1, 2, 3], [4, 1, 9]))  # True
print(is_same([1, 2, 3], [1, 9]))  # False
print(is_same([1, 2, 1], [4, 4, 1]))  # False


def is_same_improved(lst1, lst2):
    """
    Better approach - O(n)
    """
    if len(lst1) != len(lst2):
        return False

    frequency_counter1 = {}
    frequency_counter2 = {}

    for item in lst1:
        # set a key to 1, or add 1 to existing key
        frequency_counter1[item] = (frequency_counter1.get(item) or 0) + 1

    for item in lst2:
        frequency_counter2[item] = (frequency_counter2.get(item) or 0) + 1

    for key in frequency_counter1:
        # return False if key from counter 1 isn't equal to any key squared in counter 2
        if key**2 not in frequency_counter2:
            return False

        # return False if values of these keys aren't the same
        if frequency_counter2[key**2] != frequency_counter1[key]:
            return False

    return True


print('IMPROVED')
print(is_same_improved([1, 2, 3], [4, 1, 9]))  # True
print(is_same_improved([1, 2, 3], [1, 9]))  # False
print(is_same_improved([1, 2, 1], [4, 4, 1]))  # False
