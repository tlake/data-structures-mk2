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


if __name__ == '__main__':

    from timeit import timeit
    from random import shuffle

    num = 10 ** 4
    cycles = 400

    best = [x for x in range(10)] * 1000
    worst = [x for x in xrange(num ** 3 - 1, num ** 4, num ** 3)]
    average = [x for x in xrange(num)]
    shuffle(average)

    setup = (
        "from __main__ import radix_sort, num, cycles, best, worst, average"
    )

    print(
        "\nTesting best case (a list of single digit numbers), "
        "worst-case (a list of fuckload-digit numbers), and average case "
        "(just a bunch of randos).\n\n"
        "These are testing with %s numbers, %s cycles each." % (num, cycles)
    )

    best_case_time = timeit(
        'radix_sort(best)', setup=setup, number=cycles
    )
    print(
        "\nBest-case (single-digits):\n"
        "Total time: " + str(best_case_time) +
        " || Avg time: " + str(best_case_time / cycles)
    )

    worst_case_time = timeit(
        'radix_sort(worst)', setup=setup, number=cycles
    )
    print(
        "\nWorst-case (fuckloads of digits):\n"
        "Total time: " + str(worst_case_time) +
        " || Avg time: " + str(worst_case_time / cycles)
    )

    avg_case_time = timeit('radix_sort(average)', setup=setup, number=cycles)
    print(
        "\nAverage-case (just randos):\n"
        "Total time: " + str(avg_case_time) +
        " || Avg time: " + str(avg_case_time / cycles)
    )

    print(
        "\nTotal elapsed test time: " +
        str(best_case_time + worst_case_time + avg_case_time)
    )
