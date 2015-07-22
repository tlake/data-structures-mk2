# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class BSTNode(object):
    def __init__(
        self,
        val,
        parent=None,
        left_child=None,
        right_child=None
    ):
        self.val = val
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child


class BST(object):
    def __init__(self):
        self.root = None
        self._size = 0

    # will insert the value val into the BST.  If val is already
    # present, it will be ignored.
    def insert(self, val):

        if self.root is None:
            self.root = BSTNode(val=val)
            self._size = 1

        else:
            node = self.root
            while True:
                if val < node.val:
                    if val.left_child is None:
                        val.left_child = BSTNode(val=val, parent=node)
                        self._size += 1
                        break
                    else:
                        node = node.left_child
                elif val > node.val:
                    if val.right_child is None:
                        val.right_child = BSTNode(val=val, parent=node)
                        self._size += 1
                        break
                    else:
                        node = node.right_child

    # will return True if val is in the BST, False if not.
    def contains(self, val):
        if self.root is None:
            return False

        else:
            node = self.root
            while True:
                if val == node.val:
                    return True
                elif val < node.val:
                    if node.left_child is None:
                        return False
                    else:
                        node = node.left_child
                elif val > node.val:
                    if node.right_child is None:
                        return False
                    else:
                        node = node.right_child

    # will return the integer size of the BST (equal to the total number of
    # values stored in the tree), 0 if the tree is empty.
    def size(self):
        return self._size

    # will return an integer representing the total number of levels in the
    # tree. If there is one value, the depth should be 1, if two values it
    # will be 2, \if three values it may be 2 or three, depending, etc.
    # example taken from
    # http://jelices.blogspot.com/2014/05/leetcode-python-maximum-depth-of-binary.html
    def depth(self):
        if self.root is None:
            return 0

        return max(self._depth(self.root.left_child),
                   self._depth(self.root.right_child)) + 1

    def _depth(self, node):
        return max(self._depth(node.left_child),
                   self._depth(node.right_child)) + 1

    # will return an integer, positive or negative that represents how well
    # balanced the tree is. Trees which are higher on the left than the right
    # should return a positive value, trees which are higher on the right than
    # the left should return a negative value.  An ideallyl-balanced tree
    # should return 0.
    def balance(self):
        pass
