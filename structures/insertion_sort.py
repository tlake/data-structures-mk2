# -*- coding utf-8 -*-
from __future__ import unicode_literals


def insertion_sort(iterable):
    sorted_list = []

    sorted_list.append(iterable[0])

    for i in iterable[1::]:
        inserted = False

        if i > sorted_list[-1]:
            sorted_list.append(i)
            inserted = True

        while not inserted:
            for index, sorted_item in enumerate(sorted_list):
                if i <= sorted_item:
                    sorted_list.insert(index, i)
                    inserted = True
                    break

    return sorted_list
