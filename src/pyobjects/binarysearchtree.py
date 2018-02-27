"""Implements a binary search tree: a type of tree that uses an ordering on the elements of some
collection to efficiently search for items in that collection (average-case O(log n) time)."""

from .binarytree import Node, Tree


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

    def remove_Node(self, node):
        if self.left is node:
            if not self.left.left and not self.left.right:
                self.left = None
            elif not self.left.left:
                self.left = self.left.right
            elif not self.left.right:
                self.left = self.left.left
            else:
                successor = self.left.right
                while successor and successor.left:
                    successor = successor.left
                if successor:
                    temp = successor
                    self.left = successor
                    self.left.right.remove_Node(temp)
        elif self.right is node:
            if not self.right.left and not self.right.right:
                self.right = None
            elif not self.right.left:
                self.right = self.right.right
            elif not self.right.right:
                self.right = self.right.left
            else:
                successor = self.right.right
                while successor and successor.left:
                    successor = successor.left
                if successor:
                    temp = successor
                    self.right = successor
                    self.right.right.remove_Node(temp)
        elif node.compareTo(self) == -1:
            self.left.remove_Node(node)
        elif node.compareTo(self) == 1:
            self.right.remove_Node(node)
        else:
            return False
    #Comparison methods
    def compare_To(self, other):
        if self.content==other.content:
            return 0
        elif self.content > other.content:
            return 1
        return -1
    # def updateFactor(self):
    #     self.balanceFactor = height(self.left) − height(self.right)

    def rotate_right(self):
        new_root = self.left
        new_left_sub = self.left.right
        old_root = self

        old_root.left = new_left_sub
        new_root.right = old_root
        self = new_root

    def rotate_left(self):

        new_root = self.right
        new_left_sub = self.right.left
        old_root = self

        old_root.right = new_left_sub
        new_root.left = old_root
        self = new_root


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

    def remove_Node(self, node):
        if self.root is node:
            if not self.left and not self.right:
                self = None
            elif not self.left:
                self = self.right
            elif not self.right:
                self = self.left
            else:
                successor = self.right
                while successor and successor.left:
                    successor = successor.left
                if successor:
                    temp = successor
                    self = successor
                    self.right.remove_Node(temp)
        else:
            self.root.node.remove_Node(node)

    def rotate_right(self):

        new_root = self.root.left
        new_left_sub = self.root.left.right
        old_root = self.root

        self.root = new_root
        old_root.left = new_left_sub
        new_root.right = old_root

    def rotate_left(self):

        new_root = self.root.right
        new_left_sub = self.root.right.left
        old_root = self.root

        self.root = new_root
        old_root.right = new_left_sub
        new_root.left = old_root
