count = int(input())
sum = 0
for i in range(1,count+1,+1):
    iq = int(input())
    sum+=iq
    if sum/i > iq:
        print("<")
    elif sum/i<iq:
        print(">")
    else:
        print(0)