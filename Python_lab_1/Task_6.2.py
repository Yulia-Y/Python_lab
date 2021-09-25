height = int(input())
for i in range (1, height*2,2):
    print(" "*((height*2 -1 -i)//2), "*"*i, " "*((height*2 -1 -i)//2), sep="")