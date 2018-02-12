class Node:
    def __init__(self, content=None, left = None, right = None):
        self.left = left
        self.right = right
        self.content = content

    def add_Content(self, content):
        self.content = content

    def add_left(self, node):
        if self.left == None:
            self.left = node
            return true
        else:
            self.left.add_left(node)
            return true

    def add_right(self, node):
        if self.right == None:
            self.right = node
            return true
        else:
            self.right.add_right(node)
            return true
    #Uses depth first traversal, adds right child of removed node to bottom of
    #left child's tree
    def remove_Node(self, node):
        if self.left is node:
            temp = self.left.right
            self.left = self.left.left
            self.left.add_left(self, node)
            return True;
        else if self.right is node:
            tempt = self.right.right
            self.right = self.right.left
            self.right.add_left(self, node)
            return True;
        return False;
    def height(self):
        if self.left is not None:
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
            if self.root.left == null:
                self.root.left = node
                return True
            else if self.root.right == null:
                self.root.right = node
                return True
            else
                return self.root.left.add_left(node)
        return false
    def remove_Node(self, node):
        return self.root.remove_Node(self, node)
    def contains_Depth(self, node):
        if self.
    def contains_Breadth(self, node):

    def sort(self):

    def balance(self):

    def print_Tree_Depth(self):

    def print_Tree_Breadth(self):
