from .nodes import Node

class Tree:
    class TreeNode(Node):
        def __init__(self, item = None, childList = []):
            super().__init__()
            self.children = childList
        def add_Child(self, node):
            if(!self.children.contains(node))
                self.children.append(node)
                return True
            return False
        def remove_Child(self, node):
            if(self.children.remove(node) == None):
                return False
            return True
    def __init__(self, root):
