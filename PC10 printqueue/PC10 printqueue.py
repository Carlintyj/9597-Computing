##Task 2
def ValidateUserID(ID):
    if len(ID) != 9:
        return 1
    elif ID[:4] != '2015':
        return 2
    for i in ID[4:]:
        if i.isalpha():
            return 3
    else:
        return 0

##Task 3
class printJob:
    def __init__(self,userID,terminalID,filesize):
                self.__userID = userID
                self.__terminalID = terminalID
                self.__filesize = filesize
    def getUserID(self):
        return self.__userID
    def getTerminalID(self):
        return self.__terminalID
    def getFilesize(self):
        return self.__filesize
    def setUserID(self):
        newUserID = input('Enter UserID: ')
        check = ValidateUserID(newUserID)
        if check != 0:
            return 'INVALID USER ID'
        else:
            self.__userID = newUserID
    def setTerminalID(self):
        newTerminalID = input('Enter terminalID (1 to 172): ')
        if int(newTerminalID) >= 1 and int(newTerminalID) <= 172:
            self.__terminalID = newTerminalID
        else:
            return 'INVALID TERMINAL ID'
    def setFilesize(self):
        newFilesize = input('Filesize (Kbytes): ')
        if newFilesize.isdigit():
            self.__filesize = newFilesize
        else:
            return 'INVALID FILESIZE'

class printQueue:
    def __init__(self,maxsize = 5):
        self.__queue = [printJob('None','None','None') for i in range(maxsize)]
        self.__rear = maxsize-1
        self.__front = 0
        self.__size = 0
        self.__limit = maxsize -1
    def __str__(self):
        temp = self.__front
        if self.__size == 0:
            return 'No print jobs in queue\n'
        else:
            for i in range(len(self.__queue)):
                print('|{0:<5}|{1:<10}|{2:<5}|{3:<5}|'.format(i,self.__queue[i].getUserID(),self.__queue[i].getTerminalID(),self.__queue[i].getFilesize()))
            print()
            print('Front Pointer =',self.__front)
            print('Rear Pointer =',self.__rear)
            return 'Size = ' +str(self.__size)
    def add_item(self):
        if self.__size == self.__limit:
            return 'Queue Overflow\n'
        else:
            self.__queue[self.__rear].setUserID()
            self.__queue[self.__rear].setTerminalID()
            self.__queue[self.__rear].setFilesize()
            if self.__rear == self.__limit:
                self.__rear = 0
            else:
                self.__rear += 1
            self.__size += 1
            
            
                    



        
