number = int(input())
n1 = number%10
n2 = number//10%10
n3 = number//100
if n1==n2==n3:
    print("В числе все цифры одинаковые")
elif n1==n2 or n1==n3 or n2==n3:
    print("В числе две одинаковые цифры")
else:
    print("OK")