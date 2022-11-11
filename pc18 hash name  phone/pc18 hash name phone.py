class Record:
    def __init__(self, personName ='',telephoneNumber = ''):
        self.__name = personName
        self.__tel = telephoneNumber

    def getName(self):
        return self.__name
    def getTel(self):
        return self.__tel
    def setName(self, newName):
        self.__name = newName
    def setTel(self, newTel):
        self.__tel = newTel

class HashNamePhone:
    def __init__(self):
        self.__slot = [Record() for i in range(500)]
        self.readFile()

    def readFile(self):
        inFile = open('HASHEDDATA.TXT','r')
        for line in inFile:
            if line[-1] == '\n':
                line = line[:-1]
            record = line.split(',')
            self.__slot[int(record[0])].setName(record[1])
            self.__slot[int(record[0])].setTel(record[2])
        inFile.close()

    def DisplayValue(self):
        print("|{:^5}|{:^20}|{:^20}|".format('Index','PersonName','TelephoneNumber'))
        for i in range(500):
            if self.__slot[i].getName() != '':
                print("|{:^5}|{:^20}|{:^20}|".format(i,self.__slot[i].getName(),self.__slot[i].getTel()))

    def GenerateHash(self,SearchName):
        HashTotal = 0
        for i in range(len(SearchName)):
            asciiCode = ord(SearchName[i])
            HashTotal += (asciiCode*(i+1))
        return HashTotal%500

    def FindRecord(self, SearchName):
        index = self.GenerateHash(SearchName)
        while self.__slot[index].getName() != SearchName and self.__slot[index].getName() != '':
            index +=1
            if index == 500:
                index = 0
        if self.__slot[index].getName() == SearchName:
            print("|{:^5}|{:^20}|{:^20}|".format('Index','PersonName','TelephoneNumber'))
            print("|{:^5}|{:^20}|{:^20}|".format(index,self.__slot[index].getName(),self.__slot[index].getTel()))
        else:
            print(SearchName,'Not found')
##a =  HashNamePhone()
##a.GenerateHash('Tait Davinder')

