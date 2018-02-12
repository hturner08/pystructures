#Alternate to cobjects.pqueue
class H_Node(Node):

class Heap:
    def add_Root(self, node):
        if self.root is None:
            self.root = node
            return True
        return False
    def add_Node(self, node):
        if node.compare_To(self.root)>1
            temp = self.root
