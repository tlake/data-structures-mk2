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
        raise KeyError('Key is not in the table.')

    def set(self, key, value):
        """Set a key value pair in the table.

        Keys must be strings.
        If the key is already in the table, updates its value.
        """
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
        if not isinstance(key, basestring):
            raise TypeError('Keys must be strings.')
        key_sum = 0
        for letter in key:
            key_sum += ord(letter)
        return (key_sum % len(self.table_list))


if __name__ == '__main__':
    from timeit import timeit

    fh = open('/usr/share/dict/words', 'r')
    exponents = [3, 4, 5, 6, 7]
    cycles = 2

    print(
        "\nItems in /usr/share/dict/words: {words}\n"
        "Sizes of hashtables: 10^{exponents}\n"
        "Cycles per hashtable: {cycles}\n".format(
            words=len(fh.readlines()),
            exponents=exponents,
            cycles=cycles
        )
    )

    setup = '''
from __main__ import hashtime

xpon = {}
    '''

    def set_timings(xpons=exponents, cycles=cycles):
        for xpon in xpons:
            print(
                "Average time for hashtable 10^" + str(xpon) + ": " +
                str(timeit(
                    'hashtime(xpon)',
                    setup=setup.format(str(xpon)),
                    number=cycles
                ) / cycles)
            )

    def hashtime(val):
        ht = HashTable(10 ** val)

        fh.seek(0)

        for line in fh:
            ht.set(line.strip(), line.strip())

        fh.seek(0)

        for line in fh:
            ht.get(line.strip())

    set_timings()

    fh.close()
