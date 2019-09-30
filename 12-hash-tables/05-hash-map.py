#!/usr/bin/env python3


class HashTable:

    def __init__(self, size=53):
        # size should be a prime number for less collisions
        self.key_map = [None] * size

    def __str__(self):
        return str(self.key_map)

    def _hash(self, key):
        """
        Return hash value of key.

        Uses prime number for more diversity and max
        number of 100 iterations.
        """
        total = 0
        prime_number = 31
        max_iterations = min(len(key), 100)
        for i in range(max_iterations):
            char = key[i]
            value = ord(char) - 96
            total = (total + prime_number + value) % len(self.key_map)
        return total

    def set(self, key, value):
        """
        Map new key - value pair inside the hash table.
        """
        index = self._hash(key)
        if not self.key_map[index]:
            self.key_map[index] = []
        self.key_map[index].append((key, value))

    def get(self, key):
        """
        Return value for a given key if key exists.

        Otherwise return None.
        """
        index = self._hash(key)
        index_value = self.key_map[index]
        if index_value:
            for tup in index_value:
                if tup[0] == key:
                    return tup[1]
        return None

    @property
    def values(self):
        """
        Return all unique values from hash table.
        """
        values_list = []
        for i_list in self.key_map:
            if i_list:
                for j_list in i_list:
                    if j_list[1] not in values_list:
                        values_list.append(j_list[1])
        return values_list


table = HashTable(17)

table.set('indigo', '#5E84C5')
table.set('arrowtown', '#9C856D')
table.set('fuzzy wuzzy brown', '#C4405D')
table.set('Beauty Bush', '#EAB3BF')
table.set('Smoky', '#655280')
table.set('jungle green', '#2FAC9A')
table.set('polar', '#E1F9F6')
table.set('oracle', '#387A72')
table.set('atlantis', '#91C526')
table.set('hokey pokey', '##C5B826')

print(table.get('irish coffee'))  # None
print(table.get('fuzzy wuzzy brown'))  # #C4405D

print(table.values)

"""
[
    '#9C856D',
    '#2FAC9A',
    '#655280',
    '#387A72',
    '#91C526',
    '##C5B826',
    '#5E84C5',
    '#E1F9F6',
    '#EAB3BF',
    '#C4405D'
]
"""
