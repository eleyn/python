class Queue:

    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0

    def enqueue(self, x):
        self.items = self.items + [x]

    def dequeue(self):
        x = self.items[0]
        self.items = self.items[1:]
        return x

    def size(self):
        return len(self.items)

    def show_me(self):
        return self.items
