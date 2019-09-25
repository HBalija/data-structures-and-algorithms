#!/usr/bin/env python3


def collect_odd_values(lst):
    """
    Return odd values from given array.

    Function uses recursive helper method.
    """
    result = []

    def helper(sub_lst):
        # recursive function

        if not len(sub_lst):
            return
        if sub_lst[0] % 2 != 0:
            result.append(sub_lst[0])

        helper(sub_lst[1:])

    helper(lst)
    return result


print(collect_odd_values([1, 2, 4, 3, 5, 66, 77, 89]))  # [1, 3, 5, 77, 89]
