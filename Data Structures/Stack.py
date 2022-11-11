class stack(object):
    def __init__(self,limit=5):
        self.__data = []
        self.__limit = limit
    def  __str__(self):
        output = ''
        for i in range(len(self.__data)):
            output = output + '\n' +'|{:^10}|'.format(self.__data[i])
        return output
    def IsEmpty(self):
        return len(self.__data) == 0
    def push(self,data):
        if len(self.__data) < self.__limit:
            self.__data.insert(0,data)
        else:
            print('Stack is full, cannot add anymore more')
    def pop(self):
        if not self.IsEmpty():
            self.__data.pop(0)
        else:
            print('Empty stack, Nothing to pop')
    def peek(self):
        return self.__data[0]
    def size(self):
        return len(self.__data)


s1 = stack()
s1.push('apple')
s1.push('durian')
s1.push('banana')
s1.push('orange')
    
