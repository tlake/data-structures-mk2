# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class BSTNode(object):
    def __init__(
        self,
        payload,
        parent=None,
        left_child=None,
        right_child=None
    ):
        self.payload = payload
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child


class BST(object):

    # will insert the value val into the BST.  If val is already
    # present, it will be ignored.
    def insert(self, val):
        pass

    # will return True if val is in the BST, False if not.
    def contains(self, val):
        pass

    # will return the integer size of the BST (equal to the total number of
    # values stored in the tree), 0 if the tree is empty.
    def size(self):
        pass

    # will return an integer representing the total number of levels in the
    # tree. If there is one value, the depth should be 1, if two values it
    # will be 2, \if three values it may be 2 or three, depending, etc.
    def depth(self):
        pass

    # will return an integer, positive or negative that represents how well
    # balanced the tree is. Trees which are higher on the left than the right
    # should return a positive value, trees which are higher on the right than
    # the left should return a negative value.  An ideallyl-balanced tree
    # should return 0.
    def balance(self):
        pass
