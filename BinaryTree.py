class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class BinaryTree:

    def __init__(self):
        self.root = None
        self.counter = 0

    def getroot(self):
        return self.root

    def Empty(self):
        return self.root == None

    def add(self, data):
        a = Node(data)
        b = self.root
        if b == None:
            self.root = a
            self.counter += 1
            
        else:
            self._add(data,b)
                    
    def _add(self, data, node):
        if data < node.data:
            if node.left != None:
                self._add(data, node.left)
            else:
                node.left = Node(data)
                self.counter += 1

        else:
            if node.right != None:
                self._add(data, node.right)
            else:
                node.right = Node(data)
                self.counter += 1       

    def size(self):
        return self.counter

    def search(self,x):
        if self.root != None:
            return self._search(data, self.root)
        else:
            return False

    def _search(self, data, node):
        if data == node.data:
            return True
        elif data < node.data and node.left != None:
            self._search(data, node.left)
        elif data > node.data and node.right != None:
            self._search(data, node.right)
        else:
            return False



    def remove(self, x):

# if tree is empty, returns false 

        if self.root == None:
            return False

# removes first root and replaces with smallest node on the right branch and returns true 

        elif self.root.data == x:
            if self.root.left == None and self.root.right == None:
                self.root = None
            elif self.root.left != None and self.root.right == None:
                self.root = self.root.left
            elif self.root.left == None and self.root.right != None:
                self.root = self.root.right
            elif self.root.left != None and self.root.right != None:
                delNodeCurrent = self.root
                delNode = self.root.right
                while delNode.left != None:
                    delNodeCurrent = delNode
                    delNode = delNode.left

                self.root.data = delNode.data
                if delNode.right != None:
                    if delNodeCurrent.data > delNode.data:
                        delNodeCurrent.left = delNode.right
                    elif delNodeCurrent.data < delNode.data:
                        delNodeCurrent.right = delNode.right

                else:
                    if delNode.data < delNodeCurrent.data:
                        delNodeCurrent.left = None
                    else:
                        delNodeCurrent.right = None

            self.counter = self.counter - 1

            return True

        current = None
        node = self.root

# locate 

        while node != None and node.data != x:
            current = node
            if x < node.data:
                node = node.left
            elif x > node.data:
                node = node.right

# if x is not in tree

        if node == None or node.data != x:
            return False

# if node to be removed has no children

        elif node.left == None and node.right == None:
            if x < current.data:
                current.left = None
            else:
                current.right = None

            self.counter = self.counter - 1
        
            return True

# if node to be removed has right child only


        elif node.left == None and node.right != None:
            if x < current.data:
                current.left = node.right

            else:
                current.right = node.right

            self.counter = self.counter - 1

            return True

# if node to be removed has left child only

        elif node.left != None and node.right == None:
            if x < current.data:
                current.left = node.left
            else:
                current.right = node.left

            self.counter = self.counter - 1
            
            return True

# if node to be removed has 2 children 

        else:
            delNodeCurrent = node
            delNode = node.right
            while delNode.left != None:
                delNodeCurrent = delNode
                delNode = delNode.left

            node.data = delNode.data
            if delNode.right != None:
                if delNodeCurrent.data > delNode.data:
                    delNodeCurrent.left = delNode.right
                elif delNodeCurrent.data < delNode.data:
                    delNodeCurrent.right = delNode.right

            else:
                if delNode.data < delNodeCurrent.data:
                    delNodeCurrent.left = None
                else:
                    delNodeCurrent.right = None

            self.counter = self.counter - 1

            return True 

            
    
                

        
                        
                

        

            
        

            
      
    

    
                    
            
        
    

    
                
        
            
