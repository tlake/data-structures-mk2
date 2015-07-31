# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class HashTable(object):

    def __init__(self, size):
        """Initialize a hash table with the provided size."""
        self.table_list = [[] for x in xrange(size)]

    def get(self, key):
        """Return the value associated with the provided key."""
        hashed = self._hash(key)
        for item in self.table_list[hashed]:
            if key == item[0]:
                return item[1]

    def set(self, key, value):
        """Set a key value pair in the table.

        Keys must be strings.
        If the key is already in the table, updates its value.
        """
        # updates value if key is in the list
        if not isinstance(key, basestring):
            raise TypeError('Keys must be strings.')
        hashed = self._hash(key)
        bucket = self.table_list[hashed]
        found = False
        for item in bucket:
            if item[0] == key:
                item[1] = value
                found = True
                break
        if not found:
            bucket.append((key, value))

    def _hash(self, key):
        key_sum = 0
        for letter in key:
            key_sum += ord(letter)
        return (key_sum % len(self.table_list))
