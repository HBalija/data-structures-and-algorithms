#!/usr/bin/env python3


def max_sub_list_sum(lst, num):
    """
    Naive approach - O(n**2)time
    """
    if len(lst) < num:
        return None

    _max = float('-infinity')
    for i in range(len(lst) - num + 1):
        temp = 0
        for j in range(num):
            temp += lst[i + j]
        if temp > _max:
            _max = temp
    return _max


print('NAIVE')
print(max_sub_list_sum([1, 2, 5, 2, 8, 1, 5], 2))  # 10
print(max_sub_list_sum([1, 2, 5, 2, 8, 1, 5], 4))  # 17
print(max_sub_list_sum([4, 2, 1, 6], 1))  # 6
print(max_sub_list_sum([], 3))  # None


def max_sub_list_sum_imporved(lst, num):
    """
    Better approach - O(n)time
    """
    if len(lst) < num:
        return None

    max_sum = 0

    for el in lst[:num]:
        max_sum += el

    temp_sum = max_sum
    index = num

    for el in lst[num:]:
        temp_sum = temp_sum - lst[index - num] + el
        max_sum = max(max_sum, temp_sum)
        index += 1

    return max_sum


print('IMPROVED')
print(max_sub_list_sum_imporved([1, 2, 5, 2, 8, 1, 5], 2))  # 10
print(max_sub_list_sum_imporved([1, 2, 5, 2, 8, 1, 5], 4))  # 17
print(max_sub_list_sum_imporved([4, 2, 1, 6], 1))  # 6
print(max_sub_list_sum_imporved([], 3))  # None
