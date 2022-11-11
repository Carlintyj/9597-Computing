inFile = open('KEYS2.txt','r')
max = eval(input('Max (Max <= 20): '))
while max > 20:
    max = eval(input('Max (Max <= 20): '))
address = ['None']*max

for i in inFile:
    i = i.strip()
    if address[int(i)%max] == 'None':
        address[int(i)%max] = i
    else:
        count = int(i)%max
        while address[count] != 'None':
            count = (count+1)%max
        address[count] = i

for i in range(max):
    print('{:<5}|{:^10}'.format(i,address[i]))

inFile.close()

def search(ID):
    for i in range(len(address)):
        if str(ID) == address[i]:
            print(ID,'was found at index',i)
            return
    print(ID,'NOT FOUND')
        
