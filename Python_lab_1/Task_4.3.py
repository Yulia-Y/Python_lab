number = int(input())
k = 0
while number%2==0:
    k+=1
    number/=2
if number == 1:
    print(k)
else:
    print("НЕТ")