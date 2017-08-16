class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class LinkedList:

    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root == None

    def add(self, x):
        a = Node(x)
        a.setNext(self.root)
        self.root = a

    def size(self):
        current = self.root
        count = 0
        while current!= None:
            count += 1
            current = current.getNext()
        return count

    def search(self,x):
        current = self.root
        found = False
        while current!= None and found!= True:
            if current.getData() == x:
                found = True
                
            else:
                current = current.getNext()

        return found

    def remove(self,x):
        current = self.root
        previous = None
        found = False
        while not found:
            if current.getData() == x:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.root = current.getNext()
        else:
            previous.setNext(current.getNext())
            
            
                
        
