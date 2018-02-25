from .binarysearchtree import BST_Node, BST_Tree

"""Method somewhat based on tutorial: http://blog.coder.si/2014/02/how-to-implement-avl-tree-in-python.html
Partial comments are pasted in for my own reference
"""

class AVL_Node(BST_Node):
    def __init__(self, content=None, left = None, right = None):
        super.__init__(content, left, right)
        self.height = -1
        self.balance = 0

    def add_Node(self, node):

        if not self.left:
            self.left = node
        elif not self.right:
            self.right = node
        elif node.compareTo(self) == -1:
            self.left.add_Node(node)
        elif node.compareTo(self) == 1:
            self.right.add_Node(node)
        self.rebalance()

    def rebalance(self):
        """
        Rebalance tree. After inserting or deleting a node,
        it is necessary to check each of the node's ancestors for consistency with the rules of AVL
        """

        # Check if we need to rebalance the tree
        #   update height
        #   balance tree
        self.update_heights(recursive=False)
        self.update_balances(False)

        # For each node checked,
        #   if the balance factor remains −1, 0, or +1 then no rotations are necessary.
        while self.balance < -1 or self.balance > 1:
            # Left subtree is larger than right subtree
            if self.balance > 1:

                # Left Right Case -> rotate y,z to the left
                if self.left.balance < 0:
                    #     x               x
                    #    / \             / \
                    #   y   D           z   D
                    #  / \        ->   / \
                    # A   z           y   C
                    #    / \         / \
                    #   B   C       A   B
                    self.left.rotate_left()
                    self.update_heights()
                    self.update_balances()

                # Left Left Case -> rotate z,x to the right
                #       x                 z
                #      / \              /   \
                #     z   D            y     x
                #    / \         ->   / \   / \
                #   y   C            A   B C   D
                #  / \
                # A   B
                self.rotate_right()
                self.update_heights()
                self.update_balances()

            # Right subtree is larger than left subtree
            if self.balance < -1:

                # Right Left Case -> rotate x,z to the right
                if self.right.balance > 0:
                    #     y               y
                    #    / \             / \
                    #   A   x           A   z
                    #      / \    ->       / \
                    #     z   D           B   x
                    #    / \                 / \
                    #   B   C               C   D
                    self.right.rotate_right() # we're in case III
                    self.update_heights()
                    self.update_balances()

                # Right Right Case -> rotate y,x to the left
                #       y                 z
                #      / \              /   \
                #     A   z            y     x
                #        / \     ->   / \   / \
                #       B   x        A   B C   D
                #          / \
                #         C   D
                self.rotate_left()
                self.update_heights()
                self.update_balances()

    def update_heights(self, recursive=True):
        """
        Update tree height

        Tree height is max height of either left or right subtrees +1 for root of the tree
        """
        if self:
            if recursive:
                if self.left:
                    self.left.update_heights()
                if self.right:
                    self.right.update_heights()

            self.height = 1 + max(self.left.height, self.right.height)
        else:
            self.height = -1

    def update_balances(self, recursive=True):
        """
        Calculate tree balance factor

        The balance factor is calculated as follows:
            balance = height(left subtree) - height(right subtree).
        """
        if self:
            if recursive:
                if self.left:
                    self.left.update_balances()
                if self.right:
                    self.right.update_balances()

            self.balance = self.left.height - self.right.height
        else:
            self.balance = 0

    def remove_Node(self, node):
        """
        Delete key from the tree

        Let node X be the node with the value we need to delete,
        and let node Y be a node in the tree we need to find to take node X's place,
        and let node Z be the actual node we take out of the tree.

        Steps to consider when deleting a node in an AVL tree are the following:

            * If node X is a leaf or has only one child, skip to step 5. (node Z will be node X)
                * Otherwise, determine node Y by finding the largest node in node X's left sub tree
                    (in-order predecessor) or the smallest in its right sub tree (in-order successor).
                * Replace node X with node Y (remember, tree structure doesn't change here, only the values).
                    In this step, node X is essentially deleted when its internal values were overwritten with node Y's.
                * Choose node Z to be the old node Y.
            * Attach node Z's subtree to its parent (if it has a subtree). If node Z's parent is null,
                update root. (node Z is currently root)
            * Delete node Z.
            * Retrace the path back up the tree (starting with node Z's parent) to the root,
                adjusting the balance factors as needed.
        """
        if self:
            if self is node:
                if not self.left and not self.right:
                    self = None
                elif not self.left:
                    self = self.right
                elif not self.right:
                    self = self.left
                else:
                    # Find  successor as smallest node in right subtree or
                    #       predecessor as largest node in left subtree
                    successor = self.right
                    while successor and successor.left:
                        successor = successor.left

                    if successor:
                        temp = successor
                        self = successor

                        # Delete successor from the replaced node right subree
                        self.right.remove_Node(temp)

            elif node.compareTo(self) == -1:
                self.left.remove_Node(node)

            elif node.compareTo(self) == 1:
                self.right.remove_Node(node)

            # Rebalance tree
            self.rebalance()
    """Following is directly copied from tutorial"""
    def inorder_traverse(self):
        """
        Inorder traversal of the tree
            Left subree + root + Right subtree
        """
        result = []

        if not self:
            return result

        result.extend(self.left.inorder_traverse())
        result.append(self.contents)
        result.extend(self.right.inorder_traverse())

        return result

class AVL_Tree(BST_Tree):

    def add_Node(self, node):

        if not self.root:
            self.root = node
        elif node.compareTo(self.root) == -1:
            self.root.left.add_Node(node)
        elif node.compareTo(self.root) == 1:
            self.root.right.add_Node(node)
        self.rebalance()

    def rebalance(self):

        self.update_heights(recursive=False)
        self.update_balances(False)

        while self.root.balance < -1 or self.root.balance > 1:
            if self.root.balance > 1:

                if self.root.left.balance < 0:
                    self.root.left.rotate_left()
                    self.update_heights()
                    self.update_balances()

                self.rotate_right()
                self.update_heights()
                self.update_balances()

            if self.root.balance < -1:

                if self.root.right.balance > 0:
                    self.root.right.rotate_right()
                    self.update_heights()
                    self.update_balances()

                self.rotate_left()
                self.update_heights()
                self.update_balances()

    def update_heights(self, recursive=True):

        if self.root:
            if recursive:
                if self.root.left:
                    self.root.left.update_heights()
                if self.root.right:
                    self.root.right.update_heights()

            self.root.height = 1 + max(self.root.left.height, self.root.right.height)
        else:
            self.root.height = -1

    def update_balances(self, recursive=True):

        if self.root:
            if recursive:
                if self.root.left:
                    self.root.left.update_balances()
                if self.root.right:
                    self.root.right.update_balances()

            self.root.balance = self.root.left.height - self.root.right.height
        else:
            self.root.balance = 0


    def remove_Node(self, node):

        if self.root:
            if self.root is node:
                if not self.root.left and not self.root.right:
                    self.root = None
                elif not self.root.left:
                    self.root = self.root.right
                elif not self.root.right:
                    self.root = self.root.left
                else:
                    successor = self.root.right
                    while successor and successor.left:
                        successor = successor.left

                    if successor:
                        temp = successor
                        self.root = successor

                        self.root.right.remove_Node(temp)

            elif node.compareTo(self.root) == -1:
                self.root.left.remove_Node(node)

            elif node.compareTo(self.root) == 1:
                self.root.right.remove_Node(node)

            # Rebalance tree
            self.rebalance()

    def inorder_traverse(self):

        result = []

        if not self.root:
            return result

        result.extend(self.root.left.inorder_traverse())
        result.append(self.root.contents)
        result.extend(self.root.right.inorder_traverse())

        return result

    def display(self, node=None, level=0):
        if not node:
            node = self.root

        if node.right:
            self.display(node.right, level + 1)
            print ('\t' * level), ('    /')

        print ('\t' * level), node

        if node.left:
            print ('\t' * level), ('    \\')
            self.display(node.left, level + 1)
