number = int(input())
k=0
while number!=1:
    k+=1
    if number%2==0:
        number/=2
    else:
        number = 3*number+1
print(k)