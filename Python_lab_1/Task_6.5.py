count = int(input())
a=0
b=1
for i in range(count):
    a =a*temp_b + temp_a*b
    b*=temp_b
A=a
B=b
while A!=0 and B!=0:
    if A>B:
        A%=B
    else:
        B%=A
print(a//(A+B),"/",b//(A+B),sep="")