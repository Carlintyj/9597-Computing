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

class stack(object):
    def __init__(self):
        self.__start = None
    def __str__(self):
        output = ''
        if self.isEmpty():
            return 'Empty Stack'
        temp = self__start
        while temp != None:
            output = output + "|{0:^20}|\n".format(temp.getData())
            temp = temp.getPointer()
        return output

    def push(self,data):
         newNode = Node(data)
         if self.isEmpty():
             self.__start =newNode
        else:
            newNode = self.__start
            self.__start = newNode
            return 
    
    def pop(self):
        if self.isEmpty():
            print('Empty Stack')
        else:
            temp = self.__start
            self.__start  = temp.getPointer()
            return temp.getData()
