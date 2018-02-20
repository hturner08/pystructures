"""Contains code to implement a red-black tree. A red-black tree is a binary tree with additional
structure (a color, red or black, added to each node) and a special set of rules for tree operations
that guarantees immunity to the worst-case scenarios of binary trees: a linked list. It ensures that
the tree is roughly balanced, which in the real world gives it very good performance for many
things. Linux currently uses it for filesystem access, for example."""

from pyobjects.binarytree import Node, Tree


class RBT_Node(Node):
    def __init__(self, color, content=None, left = None, right = None):
        super.__init__(content,left,right)
        self.color = color
