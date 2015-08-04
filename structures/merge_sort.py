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

    midval = len(iterable) // 2
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

    result.extend(left[i:])

    result.extend(right[j:])
    return result


if __name__ == '__main__':
    from timeit import timeit
    from random import shuffle

    num = 10 ** 4
    cycles = 400

    best = [x for x in xrange(num)]
    worst = ([x for x in xrange(num - 1, -1, -2)]
             + [x for x in xrange(num, -1, -2)])
    average = [x for x in xrange(num)]
    shuffle(average)

    setup = """
from __main__ import merge_sort, _merge, num, cycles, best, worst, average

"""

    print(
        "\nTesting best case (a sorted list), worst-case (IN THEORY, a "
        "left-odd-right-even), and average case (just a bunch of randos).\n\n"
        "These are testing with %s numbers, %s cycles each." % (num, cycles)
    )

    best_case_time = timeit('merge_sort(best)', setup=setup, number=cycles)
    print(
        "\nBest-case (a sorted list):\n"
        "Total time: " + str(best_case_time) +
        " || Avg time: " + str(best_case_time / cycles)
    )

    worst_case_time = timeit('merge_sort(worst)', setup=setup, number=cycles)
    print(
        "\nWorst-case (IN THEORY, a left-odd-right-even list):\n"
        "Total time: " + str(worst_case_time) +
        " || Avg time: " + str(worst_case_time / cycles)
    )

    avg_case_time = timeit('merge_sort(average)', setup=setup, number=cycles)
    print(
        "\nAverage-case (just randos):\n"
        "Total time: " + str(avg_case_time) +
        " || Avg time: " + str(avg_case_time / cycles)
    )

    print(
        "\nTotal elapsed test time: " +
        str(best_case_time + worst_case_time + avg_case_time)
    )
