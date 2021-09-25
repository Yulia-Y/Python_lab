number = int(input())
n1 = number%10
n2 = number//10%10
n3 = number//100
maxN = max(n1, n2, n3) 
minN = min(n1, n2, n3)
if n1 != maxN and n1 != minN:
    N = n1
elif n2 != maxN and n2 != minN:
    N = n2
else:
    N = n3
if (maxN+minN)/2==N:
    print("Вы ввели красивое число")
else:
    print("Жаль, вы ввели обычное число")