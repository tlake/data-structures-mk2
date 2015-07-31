# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class HashTable(object):

    def __init__(self, size):
        self.table_list = [[] for x in xrange(size)]

    def get(self, key):
        hashed = self.hash(key)
        for item in self.table_list[hashed]:
            if key == item[0]:
                return item[1]

    def set(self, key, value):
        # updates value if key is in the list
        if not isinstance(key, basestring()):
            raise TypeError('Keys must be strings.')
        hashed = self.hash(key)
        bucket = self.table_list[hashed]
        found = False
        for item in bucket:
            if item[0] == key:
                item[1] = value
                found = True
                break
        if not found:
            bucket.append((key, value))

    def hash(self, key):
        for letter in key
