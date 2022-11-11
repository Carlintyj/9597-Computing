class Hashtable:
    def __init__(self, limit):
        self.__size = limit
        self.__data = [None]*self.__size

    def display(self):
        for i in range(self.__size):
            print("{0:^5}|{1:<20}".format(i,str(self.__data[i])))

    def isFull(self):
        return None not in self.__data
    
    def put(self, data):
        if self.isFull() == False:
            hashcode = self.hashfunction(data)
            if self.__data[hashcode] == None:
                self.__data[hashcode] = data
            else:
                nextslot = self.rehash(hashcode)
                while self.__data[nextslot] != None:
                    nextslot = self.rehash(nextslot)
                self.__data[nextslot] = data
        else:
            print('NO SPACE')

    def remove(self, data):
        hashcode = self.hashfunction(data)
        if self.__data[hashcode] == data:
            self.__data[hashcode] = None
        else:
            nextslot = self.rehash(hashcode)
            count = 0
            while self.__data[nextslot] != data and count != self.__size:
                nextslot = self.rehash(nextslot)
                count += 1
            if count != self.__size:
                self.__data[nextslot] = None
            else:
                print(data, 'not found')

    def hashfunction(self, keydata):
        total = int(0)
        for eachchar in keydata:
            total = total +ord(eachchar)
        return total%(self.__size)


    def rehash(self, oldhashcode):
        return (oldhashcode + 1) % (self.__size)

h1 = Hashtable(11)
h1.display()
