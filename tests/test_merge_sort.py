# -*- coding utf-8 -*-
from __future__ import unicode_literals
# or maybe we don't?
# ONLY TIME
#   (and maybe Cris)
#   (and maybe that other guy)
# WILL TELL US
import pytest
from structures.merge_sort import merge_sort


@pytest.fixture
def sorted_list():
    return [i for i in xrange(10)]


@pytest.fixture
def reverse_list():
    return [i for i in xrange(9, -1, -1)]


@pytest.fixture
def average_list():
    return [5, 9, 2, 4, 1, 6, 8, 7, 0, 3]


def test_sorted(sorted_list):
    merge_sort(sorted_list)
    assert sorted_list == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_worst(reverse_list):
    merge_sort(reverse_list)
    assert reverse_list == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_average(average_list):
    merge_sort(average_list)
    assert average_list == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_repeats():
    l = [3, 6, 7, 3, 9, 5, 2, 7]
    merge_sort(l)
    assert l == [2, 3, 3, 5, 6, 7, 7, 9]


def test_multiple_types():
    l = [3, 'foo', 2.8, True, []]
    # python 2 sorting is crazy
    merge_sort(l)
    assert l == [True, 2.8, 3, [], 'foo']
