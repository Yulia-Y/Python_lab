d = int(input())
m = int(input())
y = int(input())
if m > 2:
    m -= 2
elif m == 1:
    m = 12
else:
    m = 11
c = y//100
y %= 100
print((d + ((13*m - 1)//5) + y + (y//4 + c//4 - 2*c + 777))%7)
