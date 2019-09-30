#!/usr/bin/env python3


def _hash(key, list_len):
    total = 0
    prime_number = 31
    max_iterations = min(len(key), 100)
    for i in range(max_iterations):
        char = key[i]
        value = ord(char) - 96
        total = (total + prime_number + value) % list_len
    return total


print(_hash('Hello', 41))  # 11
print(_hash('hash_key', 97))  # 33
