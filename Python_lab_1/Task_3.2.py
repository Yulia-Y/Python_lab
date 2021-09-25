num1 = float(input())
num2 = float(input())
operation = input()
if operation == '+':
    print(num1+num2)
elif operation == '-':
    print(num1-num2)
elif operation == '*':
    print(num1*num2)
elif operation == '/' and num2!=0:
    print(num1/num2)
else:
    print(888888)
    