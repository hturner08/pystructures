"""Implements the AVL Tree, a type of tree similar to red-black trees that uses additional structure
to guarantee balance and reduce search time to O(log n) in the worst case."""

from binarysearchtree import BST_Node, BST_Tree


class AVL_Node(BST_Node):
    def update_Balance

class AVL_Tree(BST_Tree):
    def add_Node(self, node):
        if currenk < currentNode.key:
            if node.left is not None:
                    self.add_Node(node.left)
            else:
                    node.left = TreeNode(key,val,parent=node)
                    self.updateBalance(node.leftChild)
        else:
            if node.hasRightChild():
                    self.add_Node(key,val,node.rightChild)
            else:
                    node.rightChild = TreeNode(key,val,parent=node)
                    self.updateBalance(currentNode.rightChild)

def update_Balance(self,node):
    if node.balanceFactor > 1 or node.balanceFactor < -1:
        self.rebalance(node)
        return
    if node.parent != None:
        if node.isLeftChild():
                node.parent.balanceFactor += 1
        elif node.isRightChild():
                node.parent.balanceFactor -= 1

        if node.parent.balanceFactor != 0:
                self.updateBalance(node.parent)
