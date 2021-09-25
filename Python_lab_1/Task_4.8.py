a = 0
b = 1000
print((a+b)//2)
answer = input()
while answer != '=':
    if answer == '<':
        b = (a+b)//2
    else:
        a=(a+b)//2
    print((a+b)//2)
    answer = input()
