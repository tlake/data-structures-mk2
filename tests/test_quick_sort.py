# -*- coding utf-8 -*-
from __future__ import unicode_literals
import pytest
from structures.quick_sort import quick_sort, gbest, _piv_zero


@pytest.fixture
def sorted_list():
    return [i for i in xrange(10)]


@pytest.fixture
def equal_values_list():
    return [5, 4, 4, 5, 5, 4, 5, 5, 4, 5]


@pytest.fixture
def average_list():
    return [5, 9, 2, 4, 1, 6, 8, 7, 0, 3]


@pytest.fixture
def best_list():
    return gbest(10)


# this should be the worst case
def test_sorted(sorted_list):
    quick_sort(sorted_list)
    assert sorted_list == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# three-way partition should handle this fine
def test_many_equal_values(equal_values_list):
    quick_sort(equal_values_list)
    assert equal_values_list == [4, 4, 4, 4, 5, 5, 5, 5, 5, 5]


def test_average(average_list):
    quick_sort(average_list)
    assert average_list == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_best(best_list):
    quick_sort(best_list, _piv_zero)
    assert best_list == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# used this to confirm that our sort isn't stable
# def test_stable():
#     l = [{5: 'one'}, {6: 'one'}, {4: 'one'}, {5: 'two'}, {5: 'three'},
#          {6: 'two'}]
#     quick_sort(l)
#     assert l == [{4: 'one'}, {5: 'one'}, {5: 'two'}, {5: 'three'},
#                              {6: 'one'}, {6: 'two'}]
