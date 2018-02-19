import unittest
import pytest

class BinaryTreeTest(unittest.TestCase):

    def test_methods(self):
        node_one = Node(content = 5)
        node_two = Node(content = 4)
        node_three = Node(content = 2)
        node_four = Node(content = 10)
        node_five = Node(content = -5)
        node_six = Node(content = 20)
        tree_one = Tree(node_one)
        self.assertTrue(tree_one.add_Node(node_four), msg="None")
        self.assertTrue(tree_one.add_Node(node_two), msg="None")
        self.assertTrue(tree_one.add_Node(node_three), msg="None")
        self.assertTrue(tree_one.add_Root(node_five), msg="None")
        self.assertTrue(tree_one.contains_Depth(node_four), msg="None")
        self.assertTrue(tree_one.contains_Depth(node_five), msg="None")
        self.assertFalse(tree_one.contains_Depth(node_six), msg="None")
        self.assertTrue(tree_one.contains_Breadth(node_four), msg="None")
        self.assertTrue(tree_one.contains_Breadth(node_five), msg="None")
        self.assertFalse(tree_one.contains_Breadth(node_six), msg="None")

class BinarySearchTreeTest(unittest.TestCase):
    def intialize(self):
        self.node_one = Node(content = 5)
        self.node_two = Node(content = 4)
        self.node_three = Node(content = 2)
        self.node_four = Node(content = 10)
        self.node_five = Node(content = -5)
        self.node_six = Node(content = 20)
        self.tree_one = BST_Tree(node_one)
    def test_methods(self):
        return True
class AVLTree(unittest.TestCase):
    def intialize(self):
        return True
    def test_methods(self):
        return True
class RedBlackTree(unittest.TestCase):
    def intialize(self):
        return True
    def test_methods(self):
        return True

if __name__ == '__main__':
    unittest.main()
