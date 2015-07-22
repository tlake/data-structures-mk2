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
    btree.size = 6

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
def test_insert():
    # A new tree should have nothing in its root.
    btree = BST()
    assert btree.root is None

    # First insertion should set root to that node, and that node
    # should have no parents or children.
    btree.insert(val=7)
    assert btree.root is not None
    assert btree.root.val == 7
    assert btree.root.parent is None
    assert btree.root.left_child is None
    assert btree.root.right_child is None

    # When inserting a duplicate value, nothing should appear to happen.
    # No errors, no creating new nodes.
    btree.insert(val=7)
    assert btree.root.left_child is None
    assert btree.root.right_child is None

    # When inserting a value smaller than the root, it should go in a new
    # node as left_child to root.
    btree.insert(val=4)
    assert btree.root.left_child is not None
    assert btree.root.right_child is None
    assert btree.root.left_child.val == 4

    # When inserting a value larger than the root, it should go in a new
    # node as right_child to root.
    btree.insert(val=10)
    assert btree.root.right_child is not None
    assert btree.root.right_child.val == 10

    # This is smaller than root's right_child, and should go in that node's
    # left_child slot.
    btree.insert(val=8)
    assert btree.root.right_child.left_child is not None
    assert btree.root.right_child.left_child.val == 8


# will return True if val is in the BST, False if not.
def test_contains(create_bst):
    btree = create_bst

    # The created tree contains 1 through 6, but nothing else.
    assert btree.contains(3) is True
    assert btree.contains(6) is True
    assert btree.contains(172) is False


# will return the integer size of the BST (equal to the total number of
# values stored in the tree), 0 if the tree is empty.
def test_size(create_bst):
    btree = create_bst

    # The created tree contains six nodes
    assert btree.size() == 6

    # Adding a node should increase size by one
    btree.insert(val=10)
    assert btree.size() == 7

    # Inserting a duplicate value should not create a new node, and so
    # the size result should not change.
    btree.insert(val=10)
    assert btree.size() == 7


# will return an integer representing the total number of levels in the
# tree. If there is one value, the depth should be 1, if two values it
# will be 2, \if three values it may be 2 or three, depending, etc.
def test_depth(create_bst):
    btree = create_bst

    # The created tree has three tiers of nodes
    assert btree.depth() == 3

    # Adding 7 and 8 should extend the depth by one
    btree.insert(7)
    btree.insert(8)
    assert btree.depth() == 4

    # A new tree should have depth 0
    newtree = BST()
    assert newtree.depth() == 0


# will return an integer, positive or negative that represents how well
# balanced the tree is. Trees which are higher on the left than the right
# should return a positive value, trees which are higher on the right than
# the left should return a negative value.  An ideallyl-balanced tree
# should return 0.
def test_balance(create_bst):
    btree = create_bst

    # The created tree has one fewer node on the right side.
    # A left-heavy tree should return positive; right-heavy, negative.
    assert btree.balance > 0

    # Add a node to the right side to make it balaced
    btree.insert(7)
    assert btree.balance == 0

    # Add another node to the right side to skew it negatively
    btree.insert(8)
    assert btree.balance < 0

    # A new node should be balanced because it's empty
    newtree = BST()
    assert newtree.balance == 0
