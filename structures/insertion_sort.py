# -*- coding utf-8 -*-
from __future__ import unicode_literals


def insertion_sort(iterable):
    sorted_list = []

    sorted_list.append(iterable[0])

    for i in iterable[1::]:
        for index, s in enumerate(sorted_list):
            if i <= s:
                sorted_list.insert(index, i)
                print "inserted " + str(i)
            else:
                sorted_list.append(i)
                print "appended " + str(i)
            break

    return sorted_list
