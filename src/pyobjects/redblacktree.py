from binarytree import Node

class RBT_Node(Node):
    def __init__(self, color, content=None, left = None, right = None):
        super.__init__(content,left,right)
        self.color = color
    
