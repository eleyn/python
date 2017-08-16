class Stack:

    def __init__(self):
        self.lst = []

    def is_lst_empty(self):
        return len(self.lst) == 0

    def push(self, item):
        self.lst = [item] + self.lst 

    def pop(self):
        x = self.lst[0]
        self.lst = self.lst[1:]
        return x

    def peek(self):
        return self.lst[0]

    def size(self):
        return len(self.lst)

class Stacktest():

    def test_empty(self):
        s = Stack()
        assert s.size == 0

    def test_pushandpop(self):
        s = Stack()
        s.push(3)
        s.push(4)
        assert s.size == 2
        s.pop()
        assert s.size == 1
        assert s.lst[0] == 3
        s.pop()
        assert s.size == 0 

    def test_peek(self):
        s = Stack()
        s.push(3)
        s.push(4)
        s.push(5)
        assert s.peek[0] == 5

    def test_size(self):
        s = Stack()
        assert s.size == 0





        
        
    
        
        
        

    
    

    

    
        
