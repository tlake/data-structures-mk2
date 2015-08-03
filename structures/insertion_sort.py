# -*- coding utf-8 -*-
from __future__ import unicode_literals


def insertion_sort(iterable):
    """Return a sorted iterable.
    Takes an unsorted iterable and sorts it using the insertion method.
    """
    for i in xrange(1, len(iterable)):
        item = iterable[i]
        j = i
        while item < iterable[j - 1] and j > 0:
            iterable[j] = iterable[j - 1]
            j -= 1
        iterable[j] = item
    return iterable


if __name__ == '__main__':
    from timeit import timeit
    from random import randint

    num = 10 ** 4

    best = [x for x in xrange(num)]
    worst = [x for x in xrange(num, -1, -1)]
    average = [randint(0, num) for x in xrange(num)]

    setup = """
from __main__ import insertion_sort, num, best, worst, average

"""

    print(
        "\nTesting best case (a sorted list), worst-case (an inversely-"
        "sorted list), and average case (just a bunch of randos).\n\n"
        "These are testing with %s numbers.\n\n" % num
    )

    print(
        "Best-case (a sorted list):",
        str(timeit('insertion_sort(best)', setup=setup, number=1))
    )

    print(
        "Worst-case (an inversely-sorted list):",
        str(timeit('insertion_sort(worst)', setup=setup, number=1))
    )

    print(
        "Average (just randos):",
        str(timeit('insertion_sort(average)', setup=setup, number=1))
    )
