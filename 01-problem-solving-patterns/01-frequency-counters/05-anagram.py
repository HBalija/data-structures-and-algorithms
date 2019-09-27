#!/usr/bin/env python3

"""
Given two strings, write a function to determine if the
second string is an anagram of the first. An anagram is a word, phrase,
or name formed by rearranging the letters of another,
such as cinema, formed from iceman.

validAnagram('', '') # True
validAnagram('aaz, 'zza') # False
validAnagram('anagram', 'nagaram') # True
"""


def valid_anagram(str1, str2):
    """
    O(n)time
    """
    if len(str1) != len(str2):
        return False

    obj = {}

    for char in str1:
        obj[char] = (obj.get(char) or 0) + 1

    for char in str2:
        if obj[char] > 0:
            obj[char] -= 1
        else:
            return False

    return True


print(valid_anagram('', ''))  # True
print(valid_anagram('aaz', 'zza'))  # False
print(valid_anagram('anagram', 'nagaram'))  # True
