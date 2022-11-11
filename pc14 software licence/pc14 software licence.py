from random import *
def LicenceKey():
    mylist=[]
    for i in range(65,65+26):
        mylist.append(chr(i))
    code = ''
    for i in range(9):
        code += mylist[randint(0,25)]
    check =  0
    j = 0
    for i in code:
        j+=1
        check += ord(i)*j
    if check%11 == 10:
        code += 'X'
    else:
        code += str(check%11)
    return code
    
def main():
    ans = ''
    while ans != '3':
        ans = input('1.Purchase of a new licence for either a single-user or 3-user licence\n2.Register an aditional user to an active 3-userlicence\n3.End\n>>> ')
        if ans == '1':
            licence = input('1. Single-user\n2. 3-user licence\n>>> ')
            if licence == '1':
                key = LicenceKey()
                print(key,'generated')
                inFile = open('LICENCE-KEYS.TXT','a')
                inFile.write(key+' 1\n')
                inFile.close()
            elif licence == '2':
                key = LicenceKey()
                print(key)
                inFile = open('LICENCE-KEYS.TXT','a')
                inFile.write(key+' 3 1\n')
                inFile.close()
            
        elif ans == '2':
            licence = input('Enter Licence key: ')
            inFile = open('LICENCE-KEYS.TXT','r')
            inFile = inFile.read()
            file_list = inFile.split('\n')
            for i in file_list:
                if i[0:10] == licence:
                    code = i
                    break
                elif i == '':
                    return 'INVALID LICENCE' 
            index = file_list.index(code)
            if file_list[index][11] == '3':
                if int(code[13]) < 3:
                    file_list[index] = file_list[index][:13] +str(int(file_list[index][13]) + 1)
                    File1 = open('LICENCE-KEYS.TXT','w')
                    for i in file_list:
                        print(i,file = File1)
                    File1.close()
                    return
                else:
                    return 'Licence key has maxed out users'
            else:
                return 'INVALID LICENCE'
            print(code,'registered')
        elif ans == '3':
            pass
        else:
            print('incorrect input')

class Licence:
    def __init__(self, licenceKey = '', licenceType='', datePurchase='',name=''):
        self.__licenceKey = licenceKey
        self.__licenceType = licenceType
        self.__datePurchase = datePurchase
        self.__name = name
    def setLicenceKey(self, licenceKey):
        self.__licenceKey = licenceKey
    def getLicenceKey(self):
        return self.__licenceKey
    def setLicenceType(self, licenceType):
        self.__licenceType = licenceType
    def getLicenceType(self):
        return self.__licenceType
    def setDatePurchase(self, datePurchase):
        self.__datePurchcase  = datePurchase
    def getDatePurchase(self):
        return self.__datePurchase
    def setName(self, name):
        self.__name  = name
    def getName(self):
        return self.__name
    def display(self):
        pass
class SingleUser(Licence):
    def __init__(self, MACaddress ='', dateRegister = '',numberOfUser= 1):
        self.__MACaddress = MACaddress
        self.__dateRegister = dateRegister
        self.__numberOfUser = numberOfUser
        Licence.__init__(self, licenceKey = '', licenceType='', datePurchase='',name='')

    def setMacAddress(self, MACaddress):
        self.__MACaddress = MACaddress
    def getMacAddress(self):
        return self.__MACaddress
    def setDateRegister(self, dateRegister):
        self.__dateRegister  = dateRegister
    def getDateRegister(self):
        return self.__dateRegister
    def display(self):
        pass
    
class ThreeUser(Licence):
    def __init__(self, MACaddress ='', dateRegister = ''):
        self.__MACaddress = MACaddress
        self.__dateRegister = dateRegister
        Licence.__init__(self, licenceKey = '', licenceType='', datePurchase='',name='')

    def setMacAddress(self, MACaddress):
        self.__MACaddress = MACaddress
    def getMacAddress(self):
        return self.__MACaddress
    def setDateRegister(self, dateRegister):
        self.__dateRegister  = dateRegister
    def getDateRegister(self):
        return self.__dateRegister
    def setNumberOfUser(self, numberOfUser):
        self.__numberOfUser  = numberOfUser
    def getNumberOfUser(self):
        return self.__numberOfUser
    def display(self):
        pass
