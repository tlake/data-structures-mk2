# data-structures

[![Travis](https://travis-ci.org/tlake/data-structures-mk2.svg)](https://travis-ci.org/tlake/data-structures-mk2.svg)

Authors:

- [Tanner Lake](https://github.com/tlake)
- [Nicholas Draper](https://github.com/ndraper2)

## Summary:
A (second) repository to hold sample code for a number of classic data structures implemented in Python.


### Binary Search Tree

#### Methods:

- insert(self, val)
    * Will insert the value val into the BST.  If val is already present, it will be ignored.

- contains(self, val)
    * Will return True if val is in the BST, False if not.

- size(self)
    * Will return the integer size of the BST (equal to the total number of values stored in the
    tree), 0 if the tree is empty.

- depth(self)
    * Will return an integer representing the total number of levels in the tree. If there is one
    value, the depth should be 1, if two values it will be 2, if three values it may be 2 or three,
    depending, etc.

- balance(self)
    * Will return an integer, positive or negative that represents how well balanced the tree is.
    Trees which are higher on the left than the right should return a positive value, trees which
    are higher on the right than the left should return a negative value.  An ideally-balanced tree
    should return 0.

- in_order(self):
    * Will return a generator that performs an in-order traversal of the tree and yields each node's value.

- pre_order(self):
    * Will return a generator that performs a pre-order traversal of the tree and yields each node's value.

- post_order(self):
    * Will return a generator that performs a post-order traversal of the tree and yields each node's value.

- breadth_first(self):
    * Will return a generator that performs a breadth-first traversal of the tree and yields each node's value.

#### Resources:

For implementing `depth()`, we found the following:

http://jelices.blogspot.com/2014/05/leetcode-python-maximum-depth-of-binary.html
