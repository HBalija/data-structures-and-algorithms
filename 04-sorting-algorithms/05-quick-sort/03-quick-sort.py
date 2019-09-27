#!/usr/bin/env python3def pivot(lst, start=0):


def pivot(lst, start=0):

    pivot = lst[start]
    swap_idx = start

    for i in range(start + 1, len(lst)):
        if pivot > lst[i]:
            swap_idx += 1
            lst[i], lst[swap_idx] = lst[swap_idx], lst[i]

    lst[start], lst[swap_idx] = lst[swap_idx], lst[start]

    return swap_idx


def quick_sort(lst):

    def helper(lst, left, right):

        if left < right:
            pivot_idx = pivot(lst, left)
            helper(lst, left, pivot_idx - 1)
            helper(lst, pivot_idx + 1, right)

        return lst

    return helper(lst, 0, len(lst) - 1)


print(quick_sort([9, 4, 8, 2, 100, -3, 1, 5, 7, 6, 3]))
#  [ -3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 100 ]
