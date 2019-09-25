#!/usr/bin/env python3


def linear_search(lst, num):
    """
    Return index of element if element found.

    Otherwise return -1.
    """
    for element in enumerate(lst):
        if element[1] == num:
            return element[0]
    return -1


print(linear_search([1, 5, 3, 7, 5, 8, 9], 3))  # 2
print(linear_search([1, 5, 3, 7, 5, 8, 9], 6))  # -1
