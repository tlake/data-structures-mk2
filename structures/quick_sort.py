# -*- coding: utf-8 -*-
from __future__ import unicode_literals


def quick_sort(pivot_func=_default_pivot):
    pass


def _partition(iterable, mid):
    l, r = [0, 0]
    n = len(iterable) - 1

    while r <= n:
        if iterable[r] < mid:
            iterable[l], iterable[r] = iterable[r], iterable[l]
            l += 1
            r += 1

        elif iterable[r] > mid:
            iterable[r], iterable[n] = iterable[n], iterable[r]
            n -= 1

        else:
            r += 1
