class BookRec(object):
    def __init__(self, BookID='', Title=''):
        self.__BookID = str(BookID)
        self.__Title = str(Title)
        self.__Pointer = None
    def getBookID(self):
        return self.__BookID
    def getTitle(self):
        return self.__Title
    def getPointer(self):
        return self.__Pointer
    def setBookID(self, newBookID):
        self.__BookID = newBookID
    def setTitle(self, newTitle):
        self.__Title = newTitle
    def setPointer(self,newPointer):
        self.__Pointer = newPointer

class LinkedList(object):
    def __init__(self):
        self.__start = None
        
##    def __str__(self):
##        output = " "
##        temp = self.__start
##        while temp is not None:
##           output = output + "{:<10} - >".format(temp.getData())
##           temp = temp.getPointer()
##        output = output + "None"
##        return output
    
    def isEmpty(self):
        return self.__start == None
    
    def display(self):
        temp = self.__start
        while temp is not None:
            print("{0:^5}|{1:<10}|-> ".format(temp.getBookID(),temp.getTitle()),end='')
            temp = temp.getPointer()
        
    def addNode(self,bookID,Title):
        newBook = BookRec(bookID, Title)
        if self.__start == None:
            self.__start = newBook
        else:
            temp = self.__start
            self.__start = newBook
            newBook.setPointer(temp)
            
    def searchNode(self, bookID):
        current = self.__start
        while current is not None:
            if current.getBookID() == bookID:
                return True
            current = current.getPointer()
        return False
    
    def deleteNode(self, bookID):
        if self.__start is not None:
            previous = None
            current = self.__start
            while current.getBookID() != bookID and current.getPointer() is not None:
                previous = current
                current = current.getPointer()
            if previous is None:
                if self.__start.getBookID() == bookID:
                    self.__start = current.getPointer()
            elif current.getBookID() == bookID:
                previous.setPointer(current.getPointer())
                print(bookID, 'removed')
            else:
                print(bookID, 'not found. Nothing to remove')
        else:
            print(bookID, 'not found. Nothing to remove')
            

class Hashtable(object):
    def __init__(self,size):
        self.__size = size
        self.__slots = [None] + [LinkedList() for i in range(self.__size+1)]
    def display(self):
        for i in range(1,self.__size+1):
            print("|{0:^5}|".format(i) ,end='')
            print("{0:<20}".format(str(self.__slots[i].display())))
    def Hash(self, bookID):
        total = 0
        for i in bookID:
            total += ord(i)
        return (total%self.__size + 1)
    def put(self,ID,title):
        hashcode = self.Hash(ID)
        l = self.__slots[hashcode]
        l.addNode(ID,title)
    def remove(self,ID):
        hashcode = self.Hash(ID)
        l = self.__slots[hashcode]
        l.deleteNode(ID)
    def search(self, ID):
        hashcode = self.Hash(ID)
        l = self.__slots[hashcode]
        if l.searchNode(ID) == True:
            print(ID,'found at index',hashcode)
        else:
            print(ID,'not found in hash table.')


def Task4():
    books = Hashtable(17)
    books.put('CS733','Basic algorithms')
    books.put('AB944','Master Computing')
    books.put('KS293','Data structures')
    books.put('BK232','Programming exercises')
    books.put('PK199','Testing Python')
    books.display()
    books.remove('AB944')
    books.display()
    books.search('KS293')
