class Node(object):
    def __init__(self, Data):
        self.__data = Data
        self.__leftP = 0
        self.__rightP = 0
    def getData(self):
        return self.__data
    def getLeftP(self):
        return  self.__leftP
    def getRightP(self):
        return  self.__rightP
    def setLeftP(self, newLeft):
        self.__leftP = newLeft
    def setRightP(self,newRight):
        self.__rightP = newRight
    def setData(self, data):
        self.__data = data

class BinaryTree(object):
    def __init__(self):
        self.__ThisTree = [Node('') for i in range(21)]
        self.__Root = 0
        self.__NextFreePosition = 1
        for i in range(1,20):
            self.__ThisTree[i].setLeftP(i+1)
        self.__ThisTree[20].setLeftP(0)
        for i in range(1,21):
            self.__ThisTree[i].setRightP(0)
            
    def AddItemToBinaryTree(self,NewTreeItem):
        if self.__NextFreePosition == 0:
            print('ERROR: NO FREE NODE AVAILABLE')
        else:
            NewTreeItem = str(NewTreeItem)
            temp = self.__ThisTree[self.__NextFreePosition].getLeftP()
            self.__ThisTree[self.__NextFreePosition].setData(NewTreeItem)
            self.__ThisTree[self.__NextFreePosition].setRightP(0)
            self.__ThisTree[self.__NextFreePosition].setLeftP(0)
            current = self.__Root
            previous = current
            LastMove = 'X'       

            if self.__Root == 0:
                self.__Root = self.__NextFreePosition
            else:
                current = self.__Root
                while current != 0:
                    previous = current
                    if NewTreeItem < self.__ThisTree[current].getData():
                        LastMove = 'L'
                        current = self.__ThisTree[current].getLeftP()
                    else:
                        LastMove = 'R'
                        current = self.__ThisTree[current].getRightP()
            if LastMove == 'R':
                self.__ThisTree[previous].setRightP(self.__NextFreePosition)
            elif LastMove == 'L':
                self.__ThisTree[previous].setLeftP(self.__NextFreePosition)

            if temp != 0:
                self.__NextFreePosition = temp
            else:
                self.__NextFreePosition = 0
    def OutputData(self):
        print('The Root Value is',self.__Root)
        print('The Next Free Position is',self.__NextFreePosition)
        print('|{0:^6}|{1:^10}|{2:^15}|{3:^10}|'.format('Node','LeftP','Data','RightP'))
        for i in range(1,21):
            print('|{0:^6}|{1:^10}|{2:^15}|{3:^10}|'.format(i, self.__ThisTree[i].getLeftP(),self.__ThisTree[i].getData(),self.__ThisTree[i].getRightP()))
    def getRoot(self):
        return self.__Root
    def inOrder(self,current):
        
        if current:
            self.inOrder(self.__ThisTree[current].getLeftP())
            print(self.__ThisTree[current].getData())
            self.inOrder(self.__ThisTree[current].getRightP())


def begin():
    bt = BinaryTree()
    data = 'y'
    while True:
        data = input('Enter data to be added (XXX to end): ')
        if data == 'XXX': break
        bt.AddItemToBinaryTree(data)
    bt.OutputData()
    print('In Order:')
    a.inOrder(a.getRoot())
    

def main():
    a = BinaryTree()
    a.AddItemToBinaryTree('INDIA')
    a.AddItemToBinaryTree('NEPAL')
    a.AddItemToBinaryTree('MALAYSIA')
    a.AddItemToBinaryTree('SINGAPORE')
    a.AddItemToBinaryTree('BURMA')
    a.AddItemToBinaryTree('CANADA')
    a.AddItemToBinaryTree('LATVIA')
    a.OutputData()
    print('In Order:')
    a.inOrder(a.getRoot())
