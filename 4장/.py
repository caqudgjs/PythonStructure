from ArrayStack import ArrayStack


def infixToPostfix(expr):
    prec = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
    opStack = ArrayStack(100)
    postfixList = []
    tokenList = expr.split()

    for token in tokenList:
        if token.isnumeric():
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
                  (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return " ".join(postfixList)


def evalPostfix(expr):
    s = ArrayStack(100)
    for token in expr.split():
        if token in "+-*/":
            val2 = s.pop()
            val1 = s.pop()
            if (token == '+'):
                s.push(val1 + val2)
            elif (token == '-'):
                s.push(val1 - val2)
            elif (token == '*'):
                s.push(val1 * val2)
            elif (token == '/'):
                s.push(val1 / val2)
        else:
            s.push(float(token))

    return s.pop()


expr = input('중위표기 수식을 입력하세요: ')
postfix = infixToPostfix(expr)
result = evalPostfix(postfix)
print(f'결과: {result}')
