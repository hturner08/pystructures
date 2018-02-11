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


class Tree:
    def __init__(self, root = None):
        self.root = root
    def add_Node(self, node):
        while True:
            if self.root.left == null:
                self.root.left = node
                return True
            else
                return self.root.left.add_left(node)
        return false
    def remove_Node(self, node):
