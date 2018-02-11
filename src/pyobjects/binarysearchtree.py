class BST_Node(Node):
    #Comparison methods
    def compareTo(self, other):
        if self.content==other.content:
            return 0
        else if self.content > other.content:
            return 1
        return -1
