import unittest
import pytest

class BinaryTreeTest(unittest.TestCase):
    def initialize(self):
        self.node_one = Node(content = 5)
        self.node_two = Node(content = 4)
        self.node_three = Node(content = 2)
        self.node_four = Node(content = 10)
        self.node_five = Node(content = -5)
        self.node_six = Node(content = 20)
        self.tree_one = Tree(node_one)
    def test_methods(self):
        self.assertTrue(self.tree_one.add_Node(node_four))
        self.assertTrue(self.tree_one.add_Node(node_two))
        self.assertTrue(self.tree_one.add_Node(node_three))
        self.assertTrue(self.tree_one.add_Root(node_five))
        self.assertTrue(self.tree_one.contains_Depth(node_four))
        self.assertTrue(self.tree_one.contains_Depth(node_five))
        self.assertFalse(self.tree_one.contains_Depth(node_six))
        self.assertTrue(self.tree_one.contains_Breadth(node_four))
        self.assertTrue(self.tree_one.contains_Breadth(node_five))
        self.assertFalse(self.tree_one.contains_Breadth(node_six))

class BinarySearchTreeTest(unittest.TestCase):
    def intialize(self):

    def test_methods(self):

class AVLTree(unittest.TestCase):
    def intialize(self):

    def test_methods(self):

class RedBlackTree(unittest.TestCase):
    def intialize(self):

    def test_methods(self):


if __name__ == '__main__':
    unittest.main()
