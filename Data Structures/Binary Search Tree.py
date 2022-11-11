class Node(object):
    def __init__(self, rootData):
        self.__rootData = rootData
        self.__leftChild = None
        self.__rightChild = None
    def getRootData(self):
        return self.__rootData
    def getLeftChild(self):
        return self.__leftChild
    def getRightChild(self):
        return self.__rightChild
    def setRootData(self, newRootData):
        self.__rootData = newRootData
    def setLeftChild(self, newLeftChild):
        self.__leftChild = newLeftChild
    def setRightChild(self, newRightChild):
        self.__rightChild = newRightChild

class BinaryTree(object):
    def  __init__(self):
        self.__start = None
    def getStart(self):
        return self.__start
    def insertBST(self, data):
        newNode = Node(data)
        previous = None
        current = self.__start
        if self.__start == None:
            self.__start = newNode
        else:
            while current:
                if data < current.getRootData():
                    previous = current
                    current = current.getLeftChild()
                else:
                    previous = current
                    current = current.getRightChild()
            if previous.getRootData() > data:
                previous.setLeftChild(newNode)
            else:
                previous.setRightChild(newNode)
    def inOrder(self,current):
        if current:
            self.inOrder(current.getLeftChild())
            print(current.getRootData())
            self.inOrder(current.getRightChild())
    def preOrder(self,current):
        if current:
            print(current.getRootData())
            self.inOrder(current.getLeftChild())
            self.inOrder(current.getRightChild())
    def postOrder(self,current):
        if current:
            self.inOrder(current.getLeftChild())
            self.inOrder(current.getRightChild())
            print(current.getRootData())
    def searchBST(self, data):
        current = self.__start
        while current:
            if data == current.getRootData():
                return "{} FOUND!".format(data)
            elif data < current.getRootData():
                current = current.getLeftChild()
            else:
                current = current.getRightChild()
        return "{} NOT FOUND!".format(data)
    def display(self):
        pass


def main():
    fruits = ['mango','banana','durian','grapes','strawberry', 'apple','avocado','orange']
    bt = BinaryTree()
    for each in fruits:
        bt.insertBST(each)
    print('In Order:')
    bt.inOrder(bt.getStart())
    print()
    print('PreOrder:')
    bt.preOrder(bt.getStart())
    print()
    print('PostOrder:')
    bt.postOrder(bt.getStart())
    print()
    print(bt.searchBST('mango'))
    print(bt.searchBST('cherry'))

main()
