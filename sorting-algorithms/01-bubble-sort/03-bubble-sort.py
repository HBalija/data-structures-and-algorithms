#!/usr/bin/env python3


def bubble_sort(lst):
    i = len(lst) - 1
    no_swaps = True
    for el in range(i, -1, -1):
        j = 0
        no_swaps = True
        while j < i:
            if lst[j] > lst[j + 1]:
                no_swaps = False
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
            j += 1
        if no_swaps:
            break
        i -= 1
    return lst


# print(bubble_sort([6, 4, 15, 10]))  # [ 4, 6, 10, 15 ]
print(bubble_sort([7, 1, 2, 3, 4, 5, 6, 8]))  # [1, 2, 3, 4, 5, 6, 7, 8]
