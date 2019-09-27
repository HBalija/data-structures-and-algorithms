#!/usr/bin/env python3


# Iterative approach

def count_down_iteratively(num):
    for i in range(num, 0, -1):
        print(i)
    print('All done')


count_down_iteratively(10)
"""
10
9
8
7
6
5
4
3
2
1
All done
"""


# Recursive approach

def count_down(num):
    # base case
    if num <= 0:
        print('All done')
        return
    print(num)
    num -= 1
    # self calling
    count_down(num)


count_down(10)
"""
10
9
8
7
6
5
4
3
2
1
All done
"""
