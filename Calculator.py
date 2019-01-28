# Advanced version of basic calculator

num1 = input("Enter number 1")
num1 = int(num1)

num2 = input("Enter number 2")
num2 = int(num2)

opr = input("Enter operand")
opr = str(opr)

def basic_cal(n1, n2, op):
    if op == '+':
        return n1+n2
    if op == '-':
        return n1 - n2
    if op == '*':
        return n1 * n2
    if op == '/':
        return n1 / n2
    if op == '%':
        return n1 % n2


result = basic_cal(num1, num2, opr)

print(result)
