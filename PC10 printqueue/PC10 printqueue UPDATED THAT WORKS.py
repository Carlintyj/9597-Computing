##TASK 2 
def ValidateUserID(ThisUserID):
    if len(ThisUserID) != 9:
        return int(1)
    elif ThisUserID[0:5] != '2015_':
        return int(2)
    elif ThisUserID[5:9].isdigit() == False:
        return int(3)
    else:
        return int(0)

##while True:
##    userid = input('Enter User ID')
##    if ValidateUserID(userid) != 0:
##        print('Invalid ID')
##        continue
##    else:
##        print('ValidID, adding to print queue...')
##TASK 3
class Queue():
    def __init__(self,size = 5):
        self.slots = [None for i in range(size)]
        self.size = 0 #slots used
        self.front = 0 #pythonic
        self.rear = 0  #pythonic
        self.limit = size #no of slots available

    def __str__(self): #debugging usage only
        return str(self.slots) + str(self.front) + str(self.rear)

    def display(self):
        print('|{0:^11}|{1:^9}|{2:^10}|'.format('User ID','Terminal','Filesize'))
        for job in self.slots:
            if job == None:
                print('|{0:^32}|'.format('None'))
            else:
                print('|{0:^11}|{1:^9}|{2:^10}|'.format(job.userid,job.terminal,job.filesize))
        
    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == self.limit
    
    def push(self,item):
        if self.isFull():
            print('Print Queue Full, Baka~')
        else:
            self.slots[self.rear] = item
            self.rear += 1
            self.size += 1
            if self.rear == self.limit:
                self.rear = 0

    def pop(self):
        if self.isEmpty():
            print('Empty Queue how pop? Baka~')
        else:
            item = self.slots[self.front]
            self.slots[self.front] = None
            self.front += 1
            self.size -= 1
            if self.front == self.limit:
                self.front = 0
            return item

class PrintJob():
    def __init__(self,userid,terminal,filesize):
        self.userid = userid
        self.terminal = terminal
        self.filesize = filesize

def main():
    q = Queue()
    print('1. Next print job addded to print queue')
    print('2. Next print job output from printer')
    print('3. Current print queue displayed')
    print('4. End')
    while True:
        choice = int(input('>>>'))
        if choice == 1:
            if q.isFull():
                print('Full Print Queue, Baka!')
                continue
            while True:
                userid = input('Enter UserID: ')
                if ValidateUserID(userid) == 0:
                    break
            while True:
                terminal = int(input('Enter Terminal ID (1-172): '))
                if terminal > 0 and terminal < 173:
                    break
            while True:
                filesize = input('Enter filesize in Kbytes: ')
                if filesize.isdigit():
                    break
            newjob = PrintJob(userid,terminal,filesize)
            q.push(newjob)
        elif choice == 2:
            q.pop()
        elif choice == 3:
            q.display()
        elif choice == 4:
            break
            
            

main()
