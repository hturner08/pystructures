#Alternate to cobjects.pqueue

class H_Node(Node):


class Heap:
    def add_Root(self, node):
        if self.root is None:
            self.root = node
            return True
        return False
    def add_Node(self, node):
        if node.compare_To(self) == 1:
            temp = self
            self = node
            self.add_Node(temp)

        else if node.compare_To(self) == 0 or node.compare_To(self) == -1:
            if self.left is None:
                self.left = node

            else if self.right is None:
                self.right = node

            else if self.left.compare_To(node) == 1:
                self.left.add_Node(node)

            else if self.right.compare_To(node) == 1:
                self.right.add_Node(node)

            else if self.left.compare_To(node) == -1 or self.left.compare_To(node) == 0:
                temp = self.left
                self.left = node
                self.left.add_Node(temp)

            else:
                temp = self.right
                self.right = node
                self.right.add_Node(temp)
