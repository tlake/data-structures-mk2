# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from structures.bst import BST, BSTNode
import pytest


@pytest.fixture
def create_bst():
    btree = BST()

    n1 = BSTNode(val=1)
    n2 = BSTNode(val=2)
    n3 = BSTNode(val=3)
    n4 = BSTNode(val=4)
    n5 = BSTNode(val=5)
    n6 = BSTNode(val=6)

    btree.root = n4
    btree._size = 6

    n4.left_child = n2
    n4.right_child = n6

    n2.parent = n4
    n6.parent = n4

    n2.left_child = n1
    n2.right_child = n3

    n1.parent = n2
    n3.parent = n2

    n6.left_child = n5

    n5.parent = n6

    return btree


# will insert the value val into the BST.  If val is already
# present, it will be ignored.
def test_new_tree_is_empty():
    '''A new tree should have nothing in its root.'''

    btree = BST()

    assert btree.root is None


def test_insert_first_value():
    '''First insertion should set root to that node, and that node
    should have no parents or children.'''

    btree = BST()

    btree.insert(val=7)
    assert btree.root is not None
    assert btree.root.val == 7
    assert btree.root.parent is None
    assert btree.root.left_child is None
    assert btree.root.right_child is None


def test_insert_duplicate_value(create_bst):
    '''When inserting a duplicate value, nothing should appear to happen.
    No errors, no creating new nodes.'''

    btree = create_bst

    btree.insert(val=6)
    assert btree.root.right_child.right_child is None


def test_insert_second_value_smaller_than_root():
    '''When inserting a value smaller than the root, it should go in a new
    node as left_child to root in a tree with only root.'''

    btree = BST()

    btree.insert(val=3)
    btree.insert(val=2)

    assert btree.root.left_child is not None
    assert btree.root.right_child is None
    assert btree.root.left_child.val == 2


def test_insert_second_value_greater_than_root():
    '''When inserting a value larger than the root, it should go in a new
    node as right_child to root in a tree with only root.'''

    btree = BST()

    btree.insert(val=3)
    btree.insert(val=10)

    assert btree.root.right_child is not None
    assert btree.root.right_child.val == 10


def test_insert_value_greater_than_roots_right_child(create_bst):
    '''This is greater than root's right_child, and should go in that node's
    right_child slot.'''

    btree = create_bst

    btree.insert(val=8)
    assert btree.root.right_child.right_child is not None
    assert btree.root.right_child.right_child.val == 8


# will return True if val is in the BST, False if not.
def test_contains_when_empty():
    btree = BST()
    assert btree.contains(3) is False


def test_contains_value_at_root(create_bst):
    btree = create_bst
    assert btree.contains(3) is True


def test_contains_value_smaller_than_root(create_bst):
    btree = create_bst
    assert btree.contains(1) is True


def test_contains_value_greater_than_root(create_bst):
    btree = create_bst
    assert btree.contains(6) is True


def test_contains_nonexistant_value(create_bst):
    btree = create_bst
    assert btree.contains(172) is False


# will return the integer size of the BST (equal to the total number of
# values stored in the tree), 0 if the tree is empty.
def test_size_when_empty():
    btree = BST()
    assert btree.size() == 0


def test_size_of_created(create_bst):
    btree = create_bst
    assert btree.size() == 6


def test_size_after_insert(create_bst):
    btree = create_bst
    btree.insert(val=10)
    assert btree.size() == 7


def test_size_after_insert_duplicate(create_bst):
    btree = create_bst
    btree.insert(val=6)
    assert btree.size() == 6


# will return an integer representing the total number of levels in the
# tree. If there is one value, the depth should be 1, if two values it
# will be 2, \if three values it may be 2 or three, depending, etc.
def test_depth_when_empty():
    btree = BST()
    assert btree.depth() == 0


def test_depth_of_created(create_bst):
    btree = create_bst
    assert btree.depth() == 3


def test_depth_after_insert_which_does_not_increase_tier(create_bst):
    btree = create_bst
    btree.insert(7)
    assert btree.depth() == 3


def test_depth_after_insert_which_increases_tier(create_bst):
    btree = create_bst
    btree.insert(7)
    btree.insert(8)
    assert btree.depth() == 4


# will return an integer, positive or negative that represents how well
# balanced the tree is. Trees which are higher on the left than the right
# should return a positive value, trees which are higher on the right than
# the left should return a negative value.  An ideallyl-balanced tree
# should return 0.
def test_balance_when_empty():
    btree = BST()
    assert btree.balance() == 0


def test_balance_of_created(create_bst):
    '''The created tree has the same number of tiers on each side.
    A left-heavy tree should return positive; right-heavy, negative.'''

    btree = create_bst
    assert btree.balance() == 0


def test_balance_after_left_heavy(create_bst):
    btree = create_bst
    btree.insert(0)
    assert btree.balance() == 1


def test_balance_after_right_heavy(create_bst):
    btree = create_bst

    btree.insert(7)
    btree.insert(8)

    assert btree.balance() == -1


def test_balance_after_right_heavier(create_bst):
    btree = create_bst

    btree.insert(7)
    btree.insert(8)
    btree.insert(9)

    assert btree.balance() == -2


def test_breadth_first_traversal(create_bst):
    btree = create_bst
    t1_vals = [4]
    t2_vals = [2, 6]
    t3_vals = [1, 3, 5]

    trav_gen = btree.breadth_first()

    for x in range(btree.size()):
        if x < 1:
            assert trav_gen.next() in t1_vals
        elif x < 3:
            assert trav_gen.next() in t2_vals
        else:
            assert trav_gen.next() in t3_vals

    with pytest.raises(StopIteration):
        trav_gen.next()


def test_pre_order_traversal(create_bst):
    btree = create_bst
    expected = [4, 2, 1, 3, 6, 5]

    trav_gen = btree.pre_order()

    for x in range(btree.size()):
        assert trav_gen.next() == expected[x]

    with pytest.raises(StopIteration):
        trav_gen.next()


def test_in_order_traversal(create_bst):
    btree = create_bst
    expected = [1, 2, 3, 4, 5, 6]

    trav_gen = btree.in_order()

    for x in range(btree.size()):
        assert trav_gen.next() == expected[x]

    with pytest.raises(StopIteration):
        trav_gen.next()


def test_post_order_traversal(create_bst):
    btree = create_bst
    expected = [1, 3, 2, 5, 6, 4]

    trav_gen = btree.post_order()

    for x in range(btree.size()):
        assert trav_gen.next() == expected[x]

    with pytest.raises(StopIteration):
        trav_gen.next()


@pytest.fixture
def create_bst_2():
    btree = BST()
    vals = [10, 5, 15, 2, 7, 20, 6, 8, 17]

    for val in vals:
        btree.insert(val=val)

    return btree


def test_breadth_first_traversal_2(create_bst_2):
    btree = create_bst_2
    t1_vals = [10]
    t2_vals = [5, 15]
    t3_vals = [2, 7, 20]
    t4_vals = [6, 8, 17]

    trav_gen = btree.breadth_first()

    for x in range(btree.size()):
        if x < 1:
            assert trav_gen.next() in t1_vals
        elif x < 3:
            assert trav_gen.next() in t2_vals
        elif x < 6:
            assert trav_gen.next() in t3_vals
        else:
            assert trav_gen.next() in t4_vals

    with pytest.raises(StopIteration):
        trav_gen.next()


def test_pre_order_traversal_2(create_bst_2):
    btree = create_bst_2
    expected = [10, 5, 2, 7, 6, 8, 15, 20, 17]

    trav_gen = btree.pre_order()

    for x in range(btree.size()):
        assert trav_gen.next() == expected[x]

    with pytest.raises(StopIteration):
        trav_gen.next()


def test_in_order_traversal_2(create_bst_2):
    btree = create_bst_2
    expected = [2, 5, 6, 7, 8, 10, 15, 17, 20]

    trav_gen = btree.in_order()

    for x in range(btree.size()):
        assert trav_gen.next() == expected[x]

    with pytest.raises(StopIteration):
        trav_gen.next()


def test_post_order_traversal_2(create_bst_2):
    btree = create_bst_2
    expected = [2, 6, 8, 7, 5, 17, 20, 15, 10]

    trav_gen = btree.post_order()

    for x in range(btree.size()):
        assert trav_gen.next() == expected[x]

    with pytest.raises(StopIteration):
        trav_gen.next()


def test_delete_root(create_bst_2):
    create_bst_2.delete(10)
    assert create_bst_2.root.val == 8
    assert create_bst_2.size() == 8
    assert create_bst_2.root.parent is None


def test_delete_leaf(create_bst_2):
    create_bst_2.delete(17)
    assert not create_bst_2.contains(17)


def test_delete_one_child(create_bst_2):
    create_bst_2.delete(20)
    assert create_bst_2.root.right_child.right_child.val == 17
    assert create_bst_2.root.right_child.right_child.parent.val == 15


def test_delete_go_right(create_bst_2):
    create_bst_2.delete(5)
    assert create_bst_2.root.left_child.val == 6


def test_delete_empty_tree():
    btree = BST()
    assert btree.delete(5) is None


def test_delete_nonexistent_value(create_bst_2):
    create_bst_2.delete(25)
    assert not create_bst_2.contains(25)
    assert create_bst_2.size() == 9
