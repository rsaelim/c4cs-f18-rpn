#!/usr/bin/env python3

import operator

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}


def  calculate(myarg):
    stack = list()
    tokens = arg.split()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            val2 = stack.pop()
            val1 = stack.pop()
            result = function(val1, val2)
            stack.append(result)

    if len(stack) != 1:
        raise TypeError('Too many arguments on the stack')
    return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc> "))
        print(result)

if __name__ == '__main__':
    main()
