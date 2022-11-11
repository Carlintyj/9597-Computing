class ConnectionNode:
    def __init__(self, dataValue='',leftChild=0,rightChild=0):
        self.__dataValue = str(dataValue)
        self.__leftChild = int(leftChild)
        self.__rightChild = int(rightChild)
    def getDataValue(self):
        return self.__dataValue
    def setDataValue(self, newDataValue):
        self.__dataValue = newDataValue
    def getLeftChild(self):
        return self.__leftChild
    def setLeftChild(self, newLeftChild):
        self.__leftChild = newLeftChild
    def getRightChild(self):
        return self.__rightChild
    def setRightChild(self, newRightChild):
        self.__rightChild = newRightChild
class LinkedList:
    def __init__(self):
        self.__Root = 1
        self.__NextFreeChild = 1
        self.__RobotData = [None]+[ConnectionNode() for i in range(25)]
        for i in range(1,26):
            self.__RobotData[i].setLeftChild(i+1)
        self.__RobotData[25].setLeftChild(0)
    def OutputData(self):
        print('|{0:^5}|{1:^20}|{2:^20}|{3:^20}|'.format('Node','Data Value','Left Child','Right Child'))
        for i in range(1,26):
            print('|{0:^5}|{1:^20}|{2:^20}|{3:^20}|'.format(i,self.__RobotData[i].getDataValue(),self.__RobotData[i].getLeftChild(),self.__RobotData[i].getRightChild()))
        print('self.__Root =',self.__Root)
        print('self.__NextFreeChild =',self.__NextFreeChild)
    def FindNode(self, NodeValue):
        found = False
        CurrentPosition = self.__Root
        while found != True and CurrentPosition <= 25:
            if self.__RobotData[CurrentPosition].getDataValue() == NodeValue:
                found = True
            else:
                CurrentPosition = CurrentPosition + 1
        if CurrentPosition > 25:
            return 0
        else:
            return CurrentPosition
    def AddToRobotData(self, NewDataItem, ParentItem,ThisMove):
        if self.__Root == 1 and self.__NextFreeChild == 1:
            self.__NextFreeChild = self.__RobotData[self.__NextFreeChild].getLeftChild()
            self.__RobotData[self.__Root].setLeftChild(0)
            self.__RobotData[self.__Root].setDataValue(NewDataItem)
        else:
            ParentPosition = self.FindNode(ParentItem)
            if ParentPosition > 0:
                ExistingChild = self.FindNode(NewDataItem)
                if ExistingChild > 0:
                    ChildPointer = ExistingChild
                else:
                    ChildPointer = self.__NextFreeChild
                    self.__NextFreeChild = self.__RobotData[self.__NextFreeChild].getLeftChild()
                    self.__RobotData[ChildPointer].setLeftChild(0)
                    self.__RobotData[ChildPointer].setDataValue(NewDataItem)
                if ThisMove == 'L':
                    self.__RobotData[ParentPosition].setLeftChild(ChildPointer)
                else:
                    self.__RobotData[ParentPosition].setRightChild(ChildPointer)

    def getRoot(self):
        return self.__Root
    def preOrderTraversal(self,current):
        if current:
            print(self.__RobotData[current].getDataValue())
            self.preOrderTraversal(self.__RobotData[current].getLeftChild())
            self.preOrderTraversal(self.__RobotData[current].getRightChild())
        

def main():
    robot = LinkedList()
    inFile = open('SEARCHTREE.txt','r')
    data = inFile.read()
    data = data.split()
    for i in data:
        robot.AddToRobotData(i[0],i[2],i[4])
    robot.OutputData()
    print()
    print('Pre-order traversal: ')
    robot.preOrderTraversal(robot.getRoot())
    inFile.close()

main()
