password = int(input())
n1 = password%10
n2 = password//10%10
n3 = password//100
print(str(max((n1+n2),(n2+n3)))+str(min((n1+n2),(n2+n3))))
