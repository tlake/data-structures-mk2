# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random


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

    def get_dot(self):
        '''Recursively prepare a dot graph entry for this node.'''
        if self.left_child is not None:
            yield "\t%s -> %s;" % (self.val, self.left_child.val)
            for i in self.left_child.get_dot():
                yield i
        elif self.right_child is not None:
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (self.val, r)
        if self.right_child is not None:
            yield "\t%s -> %s;" % (self.val, self.right_child.val)
            for i in self.right_child.get_dot():
                yield i
        elif self.left_child is not None:
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (self.val, r)


class BST(object):
    def __init__(self):
        self.root = None
        self._size = 0

    def insert(self, val):
        ''' Inserts the value val into the BST.  If val is already
        present, it will be ignored.'''

        if self.root is None:
            self.root = BSTNode(val=val)
            self._size = 1

        else:
            node = self.root
            while True:
                if val < node.val:
                    if node.left_child is None:
                        node.left_child = BSTNode(val=val, parent=node)
                        self._size += 1
                        break
                    else:
                        node = node.left_child
                elif val > node.val:
                    if node.right_child is None:
                        node.right_child = BSTNode(val=val, parent=node)
                        self._size += 1
                        break
                    else:
                        node = node.right_child
                else:
                    break

    def contains(self, val):
        '''Returns True if val is in the BST, False if not.'''

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

    def size(self):
        '''Returns the integer size of the BST (equal to the total number of
        values stored in the tree), 0 if the tree is empty.'''

        return self._size

    # example taken from
    # http://jelices.blogspot.com/2014/05/leetcode-python-maximum-depth-of-binary.html
    def depth(self):
        '''Returns an integer representing the total number of levels in the
        tree. If there is one value, the depth should be 1, if two values it
        should be 2, if three values it may be 2 or three, depending, etc.
        '''

        if self.root is None:
            return 0

        return max(self._depth(self.root.left_child),
                   self._depth(self.root.right_child)) + 1

    def _depth(self, node):
        if node is None:
            return 0

        return max(self._depth(node.left_child),
                   self._depth(node.right_child)) + 1

    def balance(self):
        '''Returns an integer, positive or negative that represents how
        well balanced the tree is. Trees which are higher on the left than the
        right should return a positive value, trees which are higher on the
        right than the left should return a negative value. An
        ideally-balanced tree should return 0.'''

        if self.root is None:
            return 0

        left = self._depth(self.root.left_child)
        right = self._depth(self.root.right_child)

        return (left - right)

    def get_dot(self):
        '''Returns the tree as a dot graph for visualization'''

        return "digraph G{\n%s" % ("" if self.root is None else (
            "\t%s;\n%s\n" % (
                self.root.val,
                "\n".join(self.root.get_dot())
            )
        ))
