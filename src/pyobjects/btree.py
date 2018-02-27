from src import BST_Node, BST_Tree
import sys

class B_Node(BST_Node):
    def __init__(self, content, children = [], key_lower_bound = 0, key_upper_bound = sys.maxint):
        self.content = content
        self.children = children
        self.keys = []

class B_Tree(BST_Tree):
    def __init__(self, root = None, child_limit = 3):
        self.root = root
        self.child_limit = child_limit

    def add_Node(self, node):
        if self.root:
            if not self.is_Full(self.root):
                self.root.left.append(node)
            elif not self.is_Full(self.root.right):
                self.root.right.append(node)
            else:
                self.root.left.add_Node()
        else:
            self.root = node
    def is_Full(self,node):
        return len(node.children) == self.n
