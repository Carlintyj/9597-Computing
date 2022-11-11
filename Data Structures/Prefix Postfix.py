class stack(object):
    def __init__(self,limit=20):
        self.__data = []
        self.__limit = limit
    def  __str__(self):
        output = ''
        for i in range(len(self.__data)):
            output = output + '\n' +'|{:^10}|'.format(self.__data[i])
        return output
    def isEmpty(self):
        return len(self.__data) == 0
    def push(self,data):
        if len(self.__data) < self.__limit:
            self.__data.insert(0,data)
        else:
            print('Stack is full, cannot add anymore more')
    def pop(self):
        if not self.isEmpty():
            self.__data.pop(0)
        else:
            print('Empty stack, Nothing to pop')
    def peek(self):
        return self.__data[0]
    def size(self):
        return len(self.__data)

def infixToPostfix(infixExpression):
    operators = ['+','-','/','*']
    precedence ={'*':3, '/':3,'+':2,'-':2,'(':1}
    tokenList = infixExpression.split()
    postfixList = []
    opStack = stack()
    opStack.push('(')
    tokenList.append(')')
    for token in tokenList:
        if token.isdigit() or token.isalpha():
            print(token)
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token in operators:
            print(opStack)
            while precedence[opStack.peek()] >= precedence[token]:
                postfixList.append(opStack.peek())
                opStack.pop()
                opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(' and not opStack.isEmpty():
                postfixList.append(topToken)
                topToken = opStack.pop()
    return postfixList

def evalPostfix(postfixExpression):
    tokenList = postfixExpression.split()
    opStack = stack()
    for token in tokenList:
        if token.isdigit():
            opStack.push(token)
        elif token in '+-*/':
            x = opStack.pop()
            y = opStack.pop()
            x = float(x)
            y = float(y)
            if token =='+':
                result = y+x
            elif token == '-':
                result = y-x
            elif token == '*':
                result = y*x
            elif token == '/':
                result = y/x
            opStack.push(result)
        return opStack.pop()

print(infixToPostfix("5 * ( 6 + 2 ) - 12  / 4 "))
print(evalPostfix('5 6 2 + * 12 4 / -'))


