# -*- coding utf-8 -*-
from __future__ import unicode_literals
import pytest
from structures.quick_sort import quick_sort


@pytest.fixture
def sorted_list():
    return [i for i in xrange(10)]


@pytest.fixture
def equal_values_list():
    return [5, 4, 4, 5, 5, 4, 5, 5, 4, 5]


@pytest.fixture
def average_list():
    return [5, 9, 2, 4, 1, 6, 8, 7, 0, 3]


# this should be the worst case
def test_sorted(sorted_list):
    assert quick_sort(sorted_list) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_many_equal_values(equal_values_list):
    assert quick_sort(equal_values_list) == [4, 4, 4, 4, 5, 5, 5, 5, 5, 5]


def test_average(average_list):
    assert quick_sort(average_list) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_repeats():
    l = [3, 6, 7, 3, 9, 5, 2, 7]
    assert quick_sort(l) == [2, 3, 3, 5, 6, 7, 7, 9]
