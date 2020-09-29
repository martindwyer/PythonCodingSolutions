
from Ch3_BasicDataStructures.Ch3_01_Stack import Stack
import string

def infixToPostfix(infixExpression):
    orderPrecedence = {}
    orderPrecedence["*"] = 3
    orderPrecedence["/"] = 3
    orderPrecedence["+"] = 2
    orderPrecedence["-"] = 2
    orderPrecedence["("] = 1

    opStack = Stack()
    postfixList = []
    tokenList = infixExpression.split()

    for token in tokenList:
        if token in string.ascii_uppercase:
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while not opStack.isEmpty() and (orderPrecedence[opStack.peek()] >= orderPrecedence[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return " ".join(postfixList)


print(infixToPostfix(" ( A + B ) * ( C + D ) "))

print(infixToPostfix(" ( A + B ) * C "))

print(infixToPostfix(" A + B * C "))