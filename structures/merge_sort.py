# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# or maybe we don't?
# ONLY TIME
#   (and maybe Cris)
#   (and maybe that other guy)
# WILL TELL US


def merge_sort(iterable):
    """Return a new sorted iterable.

    Takes in an iterable and constructs a new list using the merge sort
    method.
    """
    if len(iterable) <= 1:
        return iterable

    midval = len(iterable) / 2
    left = iterable[0:midval]
    right = iterable[midval:]

    left = merge_sort(left)
    right = merge_sort(right)

    return _merge(left, right)


def _merge(left, right):
    result = []
    # adding some variables, because the other way involved a pop(0)
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1
    return result


if __name__ == '__main__':
    from timeit import timeit
    from random import shuffle

    num = 10 ** 4

    best = [x for x in xrange(num)]
    worst = [x for x in xrange(0, num, 2)] + [x for x in xrange(1, num, 2)]
    average = [x for x in xrange(num)]
    shuffle(average)

    setup = """
from __main__ import merge_sort, _merge, num, best, worst, average

"""

    print(
        "\nTesting best case (a sorted list), worst-case (an inversely-"
        "sorted list), and average case (just a bunch of randos).\n\n"
        "These are testing with %s numbers.\n" % num
    )

    print(
        "Best-case (a sorted list):",
        str(timeit('merge_sort(best)', setup=setup, number=1))
    )

    print(
        "Worst-case (an inversely-sorted list):",
        str(timeit('merge_sort(worst)', setup=setup, number=1))
    )

    print(
        "Average (just randos):",
        str(timeit('merge_sort(average)', setup=setup, number=1))
    )
