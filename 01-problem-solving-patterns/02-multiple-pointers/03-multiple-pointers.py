#!/usr/bin/env python3


def sum_zero(lst):
    """
    Naive solution - O(n**2)time, O(1)space
    """
    for i in lst:
        for j in lst[(lst.index(i) + 1):]:
            if i + j == 0:
                return [i, j]
    return None


print('NAIVE')
print(sum_zero([-3, -2, -1, 0, 1, 2, 3]))
print(sum_zero([-2, 0, 1, 3]))
print(sum_zero([-2, 0, 1, 2, 3]))


def sum_zero_improved(lst):
    """
    Improved solution -  O(n)time, O(1)space
    """
    left = 0
    right = len(lst) - 1

    while left < right:
        result = lst[left] + lst[right]

        if result == 0:
            return [lst[left], lst[right]]
        elif result > 0:
            right -= 1
        else:
            left += 1
    return None


print('IMPROVED')
print(sum_zero_improved([-3, -2, -1, 0, 1, 2, 3]))  # [-3, 3]
print(sum_zero_improved([-2, 0, 1, 3]))  # None
print(sum_zero_improved([-2, 0, 1, 2, 3]))  # [-2, 2]
print(sum_zero_improved([-1, 1]))  # [ -1, 1 ]
