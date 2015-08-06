# -*- coding utf-8 -*-
from __future__ import unicode_literals
import pytest
from structures.radix_sort import radix_sort


@pytest.fixture
def sorted_list():
    return [i for i in xrange(10)]


@pytest.fixture
def equal_values_list():
    return [
        {5: 'one'}, {6: 'one'}, {4: 'one'}, {5: 'two'}, {5: 'three'},
        {6: 'two'}
    ]


@pytest.fixture
def random_list():
    return [5, 9, 2, 4, 1, 6, 8, 7, 0, 3]


def test_sorted(sorted_list):
    radix_sort(sorted_list)
    assert sorted_list == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_average(random_list):
    radix_sort(random_list)
    assert random_list == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_stable(equal_values_list):
    radix_sort(equal_values_list)
    assert equal_values_list == [
        {4: 'one'}, {5: 'one'}, {5: 'two'}, {5: 'three'},
        {6: 'one'}, {6: 'two'}
    ]
