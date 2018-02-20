#Alternate to cobjects.pqueue
from pyobjects.binarytree import Node, Tree

from random import randint
class Max_H_Node(Node):
    def add_Node(self, node):
        if self.left is None:
            self.left = node
            return True
        elif self.right is None:
            self.right = node
            return True
        elif node.compareTo(self.left)==1:
            temp = self.left
            self.left = node
            node.left = temp
            return True
        elif node.compareTo(self.right)==1:
            temp = self.left
            self.left = node
            node.left = temp
            return True
        else:
            choose = randint(1)
            if choose == 0:
                self.left.add_Node(node)
            elif choose == 1:
                self.right.add_Node(node)
        return False

class Max_Heap:
    def add_Root(self, node):
        if self.root is None:
            self.root = node
            return True
        return False

    def add_Node(self, node):
        if node.compare_To(self.root.left) == 1:
            temp = self.root.left
            self.root.left = node
            node.left = temp
        elif node.compare_to(self.root.right) == 1:
            temp = self.root.right
            self.root.right = node
            node.right = temp
        else:
            choose = randint(1)
            if choose == 0:
                self.left.add_Node(node)
            elif choose == 1:
                self.right.add_Node(node)
