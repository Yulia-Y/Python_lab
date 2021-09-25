count = int(input())
a = 1
b = 1
for i in range (2, count+1, +1):
    a = a*(i**2) + b
    b*=(i**2)
print((3.141592653589793**2)/(a/b))
    