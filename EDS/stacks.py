class Stack:
    def __init__(self, item_list=[]):
        self.items = item_list
    def is_Empty(self):
        return self.items==[]
    def push(self, item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        if(self.is_Empty()):
            return null;
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
