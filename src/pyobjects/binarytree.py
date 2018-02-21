"""Implements a basic binary tree: a tree where each node can have two children."""
class Node:
    def __init__(self, content=None, left = None, right = None):
        self.left = left
        self.right = right
        self.content = content

    def add_Content(self, content):
        self.content = content

    def add_left(self, node):
        if self.left is None:
            self.left = node
            return True
        else:
            self.left.add_left(node)
            return True

    def add_right(self, node):
        if self.right is None:
            self.right = node
            return True
        else:
            self.right.add_right(node)
            return True
    #Uses depth first traversal, adds right child of removed node to bottom of
    #left child's tree
    def remove_Node(self, node):
        if self.left is node:
            temp = self.left.right
            self.left = self.left.left
            self.left.add_left(self, node)
            return True;
        elif self.right is node:
            tempt = self.right.right
            self.right = self.right.left
            self.right.add_left(self, node)
            return True;
        return False;
    def contains_Depth(self, node):
        if self.left is not None:
            if self.left is node:
                return True
            self.left.contains_Depth(node)
        if self.right is not None:
            if self.right is node:
                return True
            self.right.contains_Depth(node)
        return False

    def contains_Breadth(self, node):
        node_list = []
        if self.left is not None:
            if self.left is not node:
                node_list.append(self.left)
            else:
                return True
        if self.right is not None:
            if self.right is not node:
                node_list.append(self.right)
            else:
                return True
        node_list.pop().contains_Breadth(node)

    def height(self):
        if self.left is not None:
            return 1 + self.left.height()
        if self.right is not None:
            return 1 + self.left.height()

class Tree:

    def __init__(self, root = None):
        self.root = root

    def add_Root(self, node):
        if self.root == None:
            self.root = node
            return True
        else:
            node.left = self.root
            self.root = node
            return True
        return False

    def add_Node(self, node):
        while True:
            if self.root.left is None:
                self.root.left = node
                return True
            elif self.root.right is None:
                self.root.right = node
                return True
            else:
                return self.root.left.add_left(node)
        return false

    def remove_Node(self, node):
        return self.root.remove_Node(self, node)

    def contains_Depth(self, node):
        if self.left is not None:
            if self.left is node:
                return True
            self.left.contains_Depth(node)
        if self.right is not None:
            if self.right is node:
                return True
            self.right.contains_Depth(node)
        return False
    def print_Tree_Depth(self):
        print(self.root)
        if self.root.left is not None:
            self.root.left.print_Tree_Depth()
        if self.root.right is not None:
            self.root.right.print_Tree_Depth()
    #Eventually will implement using cobject.stack
    def print_Tree_Breadth(self):
        print(self.content)
        node_list = []
        if self.left is not None:
            node_list.append(self.left)
        if self.root.right is not None:
            node_list.append(self.right)
        node_list.pop().print_Tree_Breadth()
    #Eventually will implement using cobject.stack
    def contains_Breadth(self, node):
        node_list = []
        if self.left is not None:
            if self.left is not node:
                node_list.append(self.left)
            else:
                return True
        if self.right is not None:
            if self.right is not node:
                node_list.append(self.right)
            else:
                return True
        node_list.pop().contains_Breadth(node)

    def print_Tree_Depth(self):
        print(self.root.content)
        if self.root.left is not None:
            self.root.left.print_Tree_Depth()
        if self.root.right is not None:
            self.root.right.print_Tree_Depth()

    def print_Tree_Breadth(self):
        print(self.root.content)
        node_list = []
        if self.root.left is not None:
            node_list.append(self.root.left)
        if self.root.right is not None:
            node_list.append(self.root.right)
        node_list.pop().print_Tree_Breadth()
