class Node(object):
    def __init__(self, data):
        self.__data = str(data)
        self.__leftPtr = int(-1)
        self.__rightPtr = int(-1)
    def getData(self):
        return self.__data
    def setData(self,newData):
        self.__data = newData
    def getLeftPtr(self):
        return self.__leftPtr
    def setLeftPtr(self, newLeftPtr):
        self.__leftPtr = newLeftPtr
    def getRightPtr(self):
        return self.__RightPtr
    def setRightPtr(self, newRightPtr):
        self.__RightPtr = newRightPtr

class BinaryTree(object):
    def __init__(self):
        self.__Tree = [Node('') for i in range(7)]
        self.__root = -1
        self.__nextfree = 0
        for i in range(0,6):
            self.__Tree[i].setLeftPtr(i+1)
        self.__Tree[6].setLeftPtr(-1)
        for i in range(0,7):
            self.__Tree[i].setRightPtr(-1)
    def add(self, newItem):
        if self.__nextfree == -1:
            print('ERROR: NO FREE NODE AVAILABLE')
        else:
            newItem = str(newItem)
            temp = self.__Tree[self.__nextfree].getLeftPtr()
            self.__Tree[self.__nextfree].setData(newItem)
            self.__Tree[self.__nextfree].setRightPtr(-1)
            self.__Tree[self.__nextfree].setLeftPtr(-1)
            current = self.__root
            previous = current
            LastMove = 'X'

            if self.__root == -1:
                self.__root = self.__nextfree
            else:
                current = self.__root
                while current  != -1:
                    previous = current
                    if newItem < self.__Tree[current].getData():
                        LastMove = 'L'
                        current = self.__Tree[current].getLeftPtr()
                    else:
                        LastMove = 'R'
                        current = self.__Tree[current].getRightPtr()
            if LastMove == 'R':
                self.__Tree[previous].setRightPtr(self.__nextfree)
            elif LastMove =='L':
                self.__Tree[previous].setLeftPtr(self.__nextfree)
            if temp != -1:
                self.__nextfree = temp
            else:
                self.__nextfree = -1
    def __str__(self):
        print('The Root Value is',self.__root)
        print('The Next Free Position is',self.__nextfree)
        print('|{0:^6}|{1:^10}|{2:^15}|{3:^10}|'.format('Node','LeftPtr','Data','RightPtr'))
        for i in range(len(self.__Tree)):
            print('|{0:^6}|{1:^10}|{2:^15}|{3:^10}|'.format(i,self.__Tree[i].getLeftPtr(),self.__Tree[i].getData(),self.__Tree[i].getRightPtr()))
        return ''
    def inOrderTraversal(self,lmao):
        if lmao != -1:
            self.inOrderTraversal(self.__Tree[lmao].getLeftPtr())
            print(self.__Tree[lmao].getData())
            self.inOrderTraversal(self.__Tree[lmao].getRightPtr())
    def getRoot(self):
        return self.__root

def main():
    b = BinaryTree()
    b.add('Dave')
    b.add('Fred')
    b.add('Ed')
    b.add('Greg')
    b.add('Bob')
    b.add('Cid')
    b.add('Ali')
    print(b)
    print('INORDER:')
    b.inOrderTraversal(b.getRoot())
    
