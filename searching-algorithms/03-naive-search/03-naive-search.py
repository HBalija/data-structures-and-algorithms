#!/usr/bin/env python3


def naive_seacrch(long, short):
    """
    Return number of substring appearances in a string.
    """
    counter = 0

    for i in range(len(long)):
        if long[i] == short[0]:  # check if i is equal to first letter of substring
            for j in range(len(short)):
                if short[j] != long[i + j]:  # compare characters and break if no match
                    break
                if (j == len(short) - 1):  # add to counter if j iterates to substring len
                    counter += 1
    return counter


print(naive_seacrch('kaboomdboomda', 'boom'))  # 2
print(naive_seacrch('lorie loled', 'lol'))  # 1
