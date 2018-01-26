class Node:
    def __init__(self, item = None):
            self.content = item
            self.edges = []
    def get_Contents(self):
        return self.content
    def add_Contents(self, item):
        self.content = item
    def add_Edge(self, edge):
        return self.edges.append(edge)
    def remove_Edge(self, edge):
