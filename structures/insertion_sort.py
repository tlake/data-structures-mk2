# -*- coding utf-8 -*-
from __future__ import unicode_literals


def insertion_sort(iterable):
    for i in xrange(1, len(iterable)):
        item = iterable[i]
        j = i
        while item < iterable[j-1] and j > 0:
            iterable[j] = iterable[j-1]
            j -= 1
        iterable[j] = item
        print iterable, item
    return iterable
