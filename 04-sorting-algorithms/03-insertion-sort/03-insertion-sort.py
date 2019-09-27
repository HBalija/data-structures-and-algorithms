#!/usr/bin/env python3


def insertion_sort(lst):

    # start from second element
    for i in range(1, len(lst)):
        current_value = lst[i]

        # work backwards
        j = i - 1
        while j >= 0 and lst[j] > current_value:
            # while in loop, copy values to lst[j + 1] position
            lst[j + 1] = lst[j]
            j -= 1

        # set the current value
        lst[j + 1] = current_value

    return lst


print(insertion_sort([6, 4, 15, 10, 2]))  # [ 2, 4, 6, 10, 15 ]
