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


def _piv_zero(iterable):
    return 0


def quick_sort(iterable, pivot_func=_piv_eenie):
    iterable = _quick_sort(iterable)


def _quick_sort(iterable, pivot_func=_piv_eenie):
    if len(iterable) > 1:
        piv_idx = pivot_func(iterable)
        l, r, iterable = _partition(iterable, iterable[piv_idx])
        iterable[:l] = _quick_sort(iterable[:l], pivot_func)
        iterable[r:] = _quick_sort(iterable[r:], pivot_func)

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


if __name__ == '__main__':

    def gbest(size):
        mylist = [x for x in xrange(size)]
        _gbest(mylist, 0, size - 1)
        return mylist

    def _gbest(mylist, lo, hi):
        for x in xrange(lo, hi):
            assert mylist[x] == x

        if hi <= lo:
            return
        mid = lo + ((hi - lo) // 2)
        _gbest(mylist, lo, mid - 1)
        _gbest(mylist, mid + 1, hi)
        mylist[lo], mylist[mid] = mylist[mid], mylist[lo]

    from timeit import timeit
    from random import shuffle

    num = 10 ** 4
    cycles = 40

    best = gbest(num)

    worst = [x for x in xrange(num)]
    average = [x for x in xrange(num)]
    shuffle(average)

    setup = (
        "from __main__ import quick_sort, num, cycles, best, "
        "worst, average, _piv_zero"
    )

    print(
        "\nTesting best case (in theory, a custom optimized list), "
        "worst-case (an already-sorted list), and average case "
        "(just a bunch of randos).\n\n"
        "These are testing with %s numbers, %s cycles each." % (num, cycles)
    )

    best_case_time = timeit(
        'quick_sort(best, _piv_zero)', setup=setup, number=cycles
    )
    print(
        "\nBest-case (a custom optimized list):\n"
        "Total time: " + str(best_case_time) +
        " || Avg time: " + str(best_case_time / cycles)
    )

    worst_case_time = timeit(
        'quick_sort(worst, _piv_zero)', setup=setup, number=cycles
        )
    print(
        "\nWorst-case (a completely sorted list with pivot index 0):\n"
        "Total time: " + str(worst_case_time) +
        " || Avg time: " + str(worst_case_time / cycles)
    )

    avg_case_time = timeit('quick_sort(average)', setup=setup, number=cycles)
    print(
        "\nAverage-case (just randos, random pivot):\n"
        "Total time: " + str(avg_case_time) +
        " || Avg time: " + str(avg_case_time / cycles)
    )

    print(
        "\nTotal elapsed test time: " +
        str(best_case_time + worst_case_time + avg_case_time)
    )
