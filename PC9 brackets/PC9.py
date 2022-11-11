class Stack(object):
    def __init__(self):
        self.__items =[]
        self.__top = 0

    def Push(self, item):
        self.__items.append(item)
        self.__top += 1
    def Pop(self):
        if self.isEmpty():
            return 'Stack is empty. Nothing to pop.'
        self.__top -= 1
        return self.__items.pop()
    def Peep(self):
        if self.isEmpty():
            return 'Stack is empty.'
        return self.__items[self.__top -1]
    def isEmpty(self):
        return self.__top == 0

def CheckWellformed(construct):
    leftBrackets = ['(','[','{']
    rightBrackets = [')',']','}']
    opStack = Stack()
    for i in range(len(construct)):
        if construct[i] in '([{':
            opStack.Push(construct[i])
        elif construct[i] in ')]}':
            if not opStack.isEmpty():
                topItem = opStack.Pop()
                if leftBrackets.index(topItem) != rightBrackets.index(construct[i]):
                    if construct[i] in '([{':
                        return 'Expecting'+ ' '+ rightBrackets[leftBrackets.index(construct[i])]
                    else:
                        return 'Expecting'+ ' '+ leftBrackets[rightBrackets.index(construct[i])]
    if not opStack.isEmpty():
        if construct[i] in '([{':
            return 'Expecting'+ ' '+ rightBrackets[leftBrackets.index(construct[i])]
        else:
            return 'Expecting'+ ' '+ leftBrackets[rightBrackets.index(construct[i])]
    else:
        return 

            
def CheckNested(construct):
    leftBrackets = ['(','[','{']
    rightBrackets = [')',']','}']
    opStack = Stack()
    for i in range(len(construct)):
        if construct[i] in '([{':
            opStack.Push(construct[i])
        elif construct[i] in ')]}':
            if not opStack.isEmpty():
                topItem = opStack.Pop()
                if leftBrackets.index(topItem) == rightBrackets.index(construct[i]):
                    continue
                else:
                    return False
            else:
                return False
    if not opStack.isEmpty():
        return False
    else:
        return True

def task3():
    inFile = open('DATA.txt','r')
    outfile = open('ERRORS.txt','w')
    for line in inFile:
        if CheckNested(line[:-1]) is False:
            print(line[:-1], file = outfile)
        print(line)
    inFile.close()
    outfile.close()

def task4():
    inFile = open('DATA.txt','r')
    for line in inFile:
        if CheckNested(line[:-1]) is False:
            print(line[:-1])
##            print(CheckWellformed(line[:-1]))
            print()
    inFile.close()
