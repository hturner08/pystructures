class BST_Node(Node):
    def add_Node():
        if
    #Comparison methods
    def compare_To(self, other):
        if self.content==other.content:
            return 0
        else if self.content > other.content:
            return 1
        return -1

class BST_Tree:
    def add_Root(self, node):
        if self.root == None
            self.root = node
        if node.compare_To(self.root) == 1:
            node.left = self.root
            self.root = node
            return True
        else if node.compare_To(self.root) == -1:
            self.root = node.right
            self.root = node
            return True
        return False
    def add_Node():
