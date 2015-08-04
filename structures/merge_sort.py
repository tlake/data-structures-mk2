# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# or maybe we don't?
# ONLY TIME
#   (and maybe Cris)
#   (and maybe that other guy)
# WILL TELL US


def merge_sort(iterable):
    if len(iterable) <= 1:
        return iterable

    midval = len(iterable) / 2
    left = iterable[0:midval]
    right = iterable[midval:]

    left = merge_sort(left)
    right = merge_sort(right)

    _merge(left, right)


def _merge(left, right):
    pass
