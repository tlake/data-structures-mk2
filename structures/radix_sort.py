# -*- coding: utf-8 -*-
from __future__ import unicode_literals


def radix_sort(iterable, num_base=10):
    max_length = False
    tmp, decimal_place = -1, 1

    while not max_length:
        max_length = True

        buckets = [[] for x in xrange(num_base)]

        for item in iterable:
            tmp = item // decimal_place
            buckets[tmp % num_base].append(item)
            if max_length and tmp > 0:
                max_length = False

        idx = 0
        for x in xrange(num_base):
            bucket = buckets[x]
            for item in bucket:
                iterable[idx] = item
                idx += 1

        decimal_place *= num_base
