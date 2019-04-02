# Matthías Ólafur

class Node:
    def __init__(self, v):
        self.value = v
        self.left = None
        self.right = None
    def insert(self, d):
        if self.value == d:  # Eru þessi gögn þegar fyrir
            return False
        elif self.value > d:  # Förum vinstra megin
            if self.left:  # Er til leftChild
                return self.left.insert(d)
            else:
                self.left = Node(d)
                return True
        else:  # Förum hægra megin
            if self.right:  # Er til rightChild
                return self.right.insert(d)
            else:
                self.right = Node(d)
                return True
    def preOrderPrint(self):
        print(self.value,end=" ")
        if self.left:
            self.left.preOrderPrint()
        if self.right:
            self.right.preOrderPrint()
    def postOrderPrint(self):
        if self.left:
            self.left.postOrderPrint()
        if self.right:
            self.right.postOrderPrint()
        print(self.value,end=" ")
    def getEndRight(self,g):
        if self.left:
            return self.left.getEndRight(self)
        else:
            if self.right:
                g.right = self.right
            else:
                if g and g.right:
                    if g.right.value == self.value:
                        g.right = None
                if g and g.left:
                    if g.left.value == self.value:
                        g.left = None
            return self.value
    def getEndLeft(self,g):
        if self.right:
            return self.right.getEndLeft(self)
        else:
            if self.left:
                g.left = self.left
            else:
                if g and g.right:
                    if g.right.value == self.value:
                        g.right = None
                if g and g.left:
                    if g.left.value == self.value:
                        g.left = None
            return self.value
    def delete(self,g,n):
        if self.value == n:
            if self.right:
                self.value = self.right.getEndRight(self)
            elif self.left:
                self.value = self.left.getEndLeft(self)
            else:
                if g and g.right:
                    if g.right.value == self.value:
                        g.right = None
                if g and g.left:
                    if g.left.value == self.value:
                        g.left = None
            return True
        else:
            if n < self.value and self.left:
                return self.left.delete(self,n)
            elif n > self.value and self.right:
                return self.right.delete(self,n)
        return False

class Tree:
    def __init__(self):
        self.root = None
    def insert(self, d):
        if self.root:  # Er til rót?
            return self.root.insert(d)
        else:
            self.root = Node(d)
            return True
    def preOrderPrint(self):
        if self.root:
            print("Pre Order:")
            self.root.preOrderPrint()
            print()
        else:
            print("Ekkert í rót")
    def postOrderPrint(self):
        if self.root:
            print("Post Order")
            self.root.postOrderPrint()
            print()
        else:
            print("Ekkert í rót")
    def delete(self,n):
        if self.root:
            return self.root.delete(None,n)
        else:
            print("Ekkert í rót")
    def deleteTree(self):
        self.root = None

# Þinn kóði hér

t = Tree()

t.insert(10)
t.insert(5)
t.insert(20)
t.insert(3)
t.insert(8)
t.insert(4)
t.insert(8)
t.insert(9)
t.insert(6)
t.insert(15)
t.insert(25)
t.insert(30)
t.insert(23)
t.insert(35)
t.insert(34)

t.preOrderPrint()
t.postOrderPrint()

print("Delete:",t.delete(34))
t.deleteTree()
t.preOrderPrint()