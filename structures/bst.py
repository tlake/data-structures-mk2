# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random
from collections import deque


class BSTNode(object):
    """A node suitable for insertion into a binary tree.

        Values:
                val: the data stored in the node
                parent: the parent node
                left_child: the left child of the node
                right_child: the right child of the node
    """
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
    """ A binary search tree that holds BSTNodes.

        Values:
                root: the root node of the tree.

    """

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

    def delete(self, val):
        '''Removes val from the tree if present; if not present, this method is
        a no-op. Returns None in all cases.'''
        if not self.contains(val):
            return None

        self._del_rec(self.root, val)
        self._size -= 1

    def _del_rec(self, node, val):
        if val < node.val:
            self._del_rec(node.left_child, val)

        elif val > node.val:
            self._del_rec(node.right_child, val)

        else:
            if node.left_child and node.right_child:
                if self._depth(node.left_child) >= self._depth(
                        node.right_child):
                    successor = self._find_max(node.left_child)
                else:
                    successor = self._find_min(node.right_child)
                node.val = successor.val
                self._del_rec(successor, successor.val)

            elif node.left_child:
                self._delete(node, node.left_child)

            elif node.right_child:
                self._delete(node, node.right_child)

            else:
                self._delete(node)

    def _delete(self, node, child=None):
        try:
            if node == node.parent.left_child:
                node.parent.left_child = child

            else:
                node.parent.right_child = child

            if child:
                child.parent = node.parent

        except AttributeError:
            node = None

    def _find_min(self, node):
        current_node = node

        while current_node.left_child:
            current_node = current_node.left_child

        return current_node

    def _find_max(self, node):
        current_node = node

        while current_node.right_child:
            current_node = current_node.right_child

        return current_node

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

        return "digraph G{\n%s}" % ("" if self.root is None else (
            "\t%s;\n%s\n" % (
                self.root.val,
                "\n".join(self.root.get_dot())
            )
        ))

    def in_order(self):
        """Return a generator of the tree in-order.

        Performs an in-order traversal of the tree, yielding each
        node's value."""
        for x in self._in_order(self.root):
            yield x

    def _in_order(self, node):
        if node is not None:
            for x in self._in_order(node.left_child):
                yield x
            yield node.val
            for y in self._in_order(node.right_child):
                yield y

    def pre_order(self):
        """Return a generator of the tree pre-order.

        Performs a pre-order traversal of the tree, yielding each
        node's value."""
        for x in self._pre_order(self.root):
            yield x

    def _pre_order(self, node):
        if node is not None:
            yield node.val
            for x in self._pre_order(node.left_child):
                yield x
            for y in self._pre_order(node.right_child):
                yield y

    def post_order(self):
        """Return a generator of the tree post-order.

        Performs a pre-order traversal of the tree, yielding each
        node's value."""
        for x in self._post_order(self.root):
            yield x

    def _post_order(self, node):
        if node is not None:
            for x in self._post_order(node.left_child):
                yield x
            for y in self._post_order(node.right_child):
                yield y
            yield node.val

    def breadth_first(self):
        """Return a generator of the tree, breadth-first.

        Performs a breadth-first traversal of the tree, yielding each
        node's value."""
        q = deque()
        q.appendleft(self.root)
        while q:
            node = q.pop()
            yield node.val
            if node.left_child is not None:
                q.appendleft(node.left_child)
            if node.right_child is not None:
                q.appendleft(node.right_child)


if __name__ == '__main__':
    # to make a graph, install graphviz and call
    # dot -Tpng test.gv -o testGraph.png from shell
    btree = BST()
    for i in range(50):
        btree.insert(random.randint(1, 100))
    dot_graph = btree.get_dot()
    with open('test.gv', 'w') as fh:
        fh.write(dot_graph)

    # running this file several times will give you a variety of graph orders
    # you can make the graph png to compare time and graph order
    from timeit import Timer
    print ('Searching for a number in a randomly distributed graph, '
           '1000 times.')
    print Timer('btree.contains(50)',
                'from __main__ import btree').timeit(1000)
    badtree = BST()
    for i in range(50):
        badtree.insert(i)
    print ('Searching for a number in a the worst possible case, '
           '1000 times.')
    print Timer('badtree.contains(50)',
                'from __main__ import badtree').timeit(1000)
