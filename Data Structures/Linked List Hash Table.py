class Node(object):
    def __init__(self, data): 
        self.__data=data   
        self.__pointer=  None
    def getData(self):
        return self.__data
    def setData(self, NewData):
        self.__data=NewData
    def getPointer(self):
        return self.__pointer
    def setPointer(self,NewPtr):
        self.__pointer=NewPtr 

class LinkedList:
    def __init__(self):
        self.__start =  None

    def __str__(self):
        output = " "
        temp = self.__start
        while temp is not None:
           output = output + "{:<10} - >".format(temp.getData())
           temp = temp.getPointer()
        output = output + "None"
        return output

    def display(self):
        temp = self.__start
        while temp is not None:
            print("{0:<10} - >".format(temp.getData()))
            temp = temp.getPointer()
        print('None')


    def addNode(self, data):
        newNode = Node(data)
        if self.__start == None:
            self.__start = newNode
        else:
            temp = self.__start
            self.__start = newNode
            newNode.setPointer(temp)

    def removeNode(self, data):
        if self.__start is not None:
            previous = None
            current = self.__start
            while current.getData() != data and current.getPointer() is not None:
                previous = current
                current = current.getPointer()
            if previous is None:
                if self.__start.getData() == data:
                    self.__start = current.getPointer()
            elif current.getData() == data:
                previous.setPointer(current.getPointer())
                print(data, 'removed')
            else:
                print(data, 'not found. Nothing to remove')
        else:
            print(data, 'not found. Nothing to remove')

    def searchNode(self, data):
        current = self.__start
        while current is not None:
            if current.getData() == data:
                return True
            current = current.getPointer()
        return False
            
            

class Hashtable:
    def __init__(self,limit):
        self.__size = limit
        self.__slots = [LinkedList() for i in range(self.__size)]

    def display(self):
        for i in range(self.__size):
            print('{}|{}'.format(i,str(self.__slots[i])))

    def put(self, data):
        hashcode = self.hashfunction(data)
        thislist = self.__slots[hashcode]
        thislist.addNode(data)

    def remove(self, data):
        hashcode = self.hashfunction(data)
        thislist = self.__slots[hashcode]
        thislist.removeNode(data)

    def hashfunction(self, keydata):
        total = int(0)
        for eachchar in keydata:
            total = total + ord(eachchar)
        return total%(self.__size)

    def search(self, data):
        hashcode = self.hashfunction(data)
        thislist = self.__slots[hashcode]
        if thislist.searchNode(data):
            print(data,'found at index',hashcode)
        else:
            print(data,'not fofund in hash table.')

