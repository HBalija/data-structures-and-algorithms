#!/usr/bin/env python3


def merge(lst1, lst2):

    results = []
    i = 0
    j = 0

    while i < len(lst1) and j < len(lst2):

        if lst1[i] <= lst2[j]:
            results.append(lst1[i])
            i += 1
        else:
            results.append(lst2[j])
            j += 1

    # append remaining values of lst1 or lst2
    while i < len(lst1):
        results.append(lst1[i])
        i += 1

    while j < len(lst2):
        results.append(lst2[j])
        j += 1

    return results


def merge_sort(lst):

    if len(lst) <= 1:
        return lst

    # split list in two parts until base condition is met
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    # merge sorted lists
    return merge(left, right)


print(merge_sort([10, 25, 76, 73, 72, 1, 8]))  # [1, 8, 10, 25, 72, 73, 76]
