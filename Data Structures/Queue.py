class Queue:
    def __init__(self):
        self.__data = []
        self.__limit = eval(input('Enter size of queue:\n>>> '))
        for i in range(self.__limit):
            self.__data.append('')
        self.__limit -= 1
        self.__front = 0
        self.__rear = 0
        self.__size = 0
    def __str__(self):
        for i in range(len(self.__data)):
            print('|{0:^10}|'.format(i),end='')
        print()
        for i in range(len(self.__data)):
            print('|{0:^10}|'.format(self.__data[i]),end='')
        print()
        print('Front Pointer =',self.__front)
        print('Rear Pointer =',self.__rear)
        return 'Size = ' + str(self.__size)
    def insert(self, data):
        if self.__size == self.__limit + 1:
            print('OVERFLOW')
            return
        else:
            self.__data[self.__rear] = data
            if self.__rear == self.__limit:
                self.__rear = 0
            else:
                self.__rear += 1
            self.__size += 1
    def delete(self):
        if self.__size == 0:
            print('UNDERFLOW')
            return
        else:
            item = self.__data[self.__front]
            self.__data[self.__front] = '**'
            self.__size -= 1
            if self.__front == self.__limit:
                self.__front = 0
            else:
                self.__front += 1

def main():
    x = True
    while x == True:
        ans = input('\n1. Initialize Queue\n2. Add Queue\n3. Delete Queue\n4. Display Queue\nx. Exit\n>>> ')
        if ans.isdigit():
            ans = int(ans)
            if ans >= 1 and ans <= 4:
                if ans == 1:
                    q = Queue()
                if ans == 2:
                    value = input('Enter data to insert\n>>> ')
                    q.insert(value)
                if ans == 3:
                    q.delete()
                if ans == 4:
                    print(q)
            else:
                print('Enter Valid Response\n')
        elif ans.upper() == 'X':
            x = False
        else:
            print('Enter Valid Response\n')

main()
