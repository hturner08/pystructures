"""Implements a binary search tree: a type of tree that uses an ordering on the elements of some
collection to efficiently search for items in that collection (average-case O(log n) time)."""

from . import Node, Tree


class BST_Node(Node):
    def add_Node(self, node):
        if self.right is None and node.compare_To(self) == 1:
            self.right = node

        elif self.right is not None and node.compare_To(self) == 1:
            self.right.add_Node(node)

        elif self.left is None and node.compare_To(self) == -1:
            self.left = node

        elif self.root.left is not None and node.compare_To(self) == -1:
            self.left.add_Node(node)

        else:
            return False

    def delete_Node(self, node):
        if self.right is None and self.left is None:
            self = None
    #Comparison methods
    def compare_To(self, other):
        if self.content==other.content:
            return 0
        elif self.content > other.content:
            return 1
        return -1
    # def updateFactor(self):
    #     self.balanceFactor = height(self.left) − height(self.right)

class BST_Tree(Tree):
    def add_Root(self, node):
        if self.root is None:
            self.root = node
        if node.compare_To(self.root) == 1:
            node.left = self.root
            self.root = node
            return True
        elif node.compare_To(self.root) == -1:
            self.root = node.right
            self.root = node
            return True
        return False
    def add_Node(self, node):
        if self.root.right is None and node.compare_To(self.root) == 1:
            self.root.right = node

        elif self.root.right is not None and node.compare_To(self.root) == 1:
            self.root.right.add_Node(node)

        elif self.root.left is None and node.compare_To(self.root) == -1:
            self.root.left = node

        elif self.root.left is not None and node.compare_To(self.root) == -1:
            self.root.left.add_Node(node)

        else:
            return False
