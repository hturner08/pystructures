class Queue:
    def __init__(self,item_list=[]):
        self.items = item_list
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        return self.items.pop(self.items[0])
