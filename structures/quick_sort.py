# -*- coding: utf-8 -*-
from __future__ import unicode_literals


def _piv_eenie(iterable):
    """
    Eenie, meenie, miney, moe
    Catch a tiger by the toe
    If he hollers, let him go
    Eenie, meenie, miney, moe

    Pick the sixteenth element, modulo iterable length.
    """
    return 15 % len(iterable)


def quick_sort(iterable, pivot_func=_piv_eenie):
    if len(iterable) > 1:
        piv_idx = pivot_func(iterable)
        l, r, iterable = _partition(iterable, iterable[piv_idx])
        iterable[:l] = quick_sort(iterable[:l], pivot_func)
        iterable[r:] = quick_sort(iterable[r:], pivot_func)
    return iterable


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
    return (l, r, iterable)
