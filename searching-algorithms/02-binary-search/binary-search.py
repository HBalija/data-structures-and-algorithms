#!/usr/bin/env python3


def binary_search(lst, num):

    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = (left + right) // 2
        if num == lst[mid]:
            return mid
        if num < lst[mid]:
            right = mid - 1
        elif num > lst[mid]:
            left = mid + 1
    return -1


print(binary_search([1, 2, 4, 6, 8, 9, 11, 14, 16, 19, 22, 57], 19))  # 9
print(binary_search([1, 4, 5, 6, 8, 9, 10, 12], 3))  # -1
