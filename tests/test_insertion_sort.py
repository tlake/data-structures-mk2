# -*- coding utf-8 -*-
from __future__ import unicode_literals
import pytest
from structures.insertion_sort import insertion_sort


@pytest.fixture
def sorted_list(self):
    return [i for i in xrange(10)]


@pytest.fixture
def reverse_list(self):
    return [i for i in xrange(9, -1, -1)]


@pytest.fixture
def average_list(self):
    return [5, 9, 2, 4, 1, 6, 8, 7, 0, 3]


def test_sorted(self, sorted_list):
    assert insertion_sort(sorted_list) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_worst(self, reverse_list):
    assert insertion_sort(reverse_list) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_average(self, average_list):
    assert insertion_sort(average_list) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_repeats(self):
    l = [3, 6, 7, 3, 9, 5, 2, 7]
    assert insertion_sort(l) == [2, 3, 3, 5, 6, 7, 7, 9]


def test_multiple_types(self):
    l = [3, 'foo', 2.8, True, []]
    # python 2 sorting is crazy
    assert insertion_sort(l) == [True, 2.8, 3, [], 'foo']
