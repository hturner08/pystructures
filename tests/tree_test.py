import unittest
import pytest

class BinaryTreeTest(unittest.TestCase):
    def initialize(self):
        self.node_one = new Node(content = 5)
        self.node_two = new Node(content = 4)
        self.node_three = new Node(content = 2)
        self.node_four = new Node(content = 10)
        self.node_five = new Node(content = -5)
        self.node_six = new Node(content = 20)
        self.tree_one = new Tree(node_one)
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

class AVLTree(unittest.TestCase):

class RedBlackTree(unittest.TestCase):


if __name__ == '__main__':
    unittest.main()
