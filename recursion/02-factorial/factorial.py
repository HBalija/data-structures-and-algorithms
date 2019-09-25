#!/usr/bin/env python3

"""
FACTORIAL

4! = 4 * 3 * 2 * 1 // 24

3! = 3 * 2!
"""


# Iterative

def factorial_iteratively(num):
    total = 1
    for i in range(1, num + 1):
        total *= i
    return total


print(factorial_iteratively(4))  # 24


# Recursion

def factorial(num):
    if num == 1:
        return num
    return num * factorial(num - 1)


print(factorial(4))  # 24
