inFile = open('equation.txt','r')
equation = inFile.read()[:-1]
equation = '4-3x=9'
number = ''
variable = 0
constant=0
equal = int(1)
for char in equation:
    if char.isdigit():
        number+= char
    elif char.isalpha():
        if number == '' or number =='-':
            number+='1'
        variable -= (int(number)*equal)
        number = ''
    elif char in ['-','+','=']:
        if number != '':
            constant+= int(number)*equal
            number = ''
        elif char == '-':
            number ='-'
        elif char == '+':
            number = '+'
        elif char == '=':
            equal = int(-1)

inFile.close()
