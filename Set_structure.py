class Set:

    def __init__(self):
        self.sets = []

    def show_me(self):
        return self.sets

    def add(self, x):
        if x not in self.sets:
            self.sets = self.sets + [x]

    def remove(self, x):
        if x not in self.sets:
            self.sets = self.sets
        elif x == self.sets[0]:
            self.sets = self.sets[1:]
        elif x == self.sets[-1]:
            self.sets = self.sets[0:-1]
        else:
            for i in range(1,len(self.sets) - 2):
                if x == self.sets[i]:
                    self.sets = self.sets[:i] + self.sets[i+1:]

    def contains(self, x):
        return x in self.sets
