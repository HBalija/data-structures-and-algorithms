#!/usr/bin/env python3


def get_digit(num, position):
    """
    Return the digit based on given position in number.

    Most right position of number is 0.
    """
    return abs(num) // pow(10, position) % 10


def count_digits(num):
    """
    Return the number of digits in a number.
    """
    return len(str(abs(num)))


def get_most_digits(lst):
    """
    Return the number of digits of largest number in list.
    """
    most_digits = 0
    for item in lst:
        most_digits = max(most_digits, count_digits(item))
    return most_digits


""" End helper methods """


def radix_sort(lst):

    # get the number of most digits of array elements (will be number of iterations)
    most_digits = get_most_digits(lst)

    for i in range(0, most_digits):

        # create 10 buckets
        # temp_lst = [[], [], [], [], [], [], [], [], [], []]
        temp_lst = [[] for l in range(10)]

        # place numbers in buckets based on digit in iteration
        for el in lst:
            digit = get_digit(el, i)
            temp_lst[digit].append(el)

        # merge the buckets into a single list
        lst = [item for sublist in temp_lst for item in sublist]
    return lst


print(radix_sort([34, 3456, 76, 239, 9, 0, 63]))
# [ 0, 9, 34, 63, 76, 239, 3456 ]
