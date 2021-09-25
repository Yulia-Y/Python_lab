height = int(input())
width = int(input())
symb = input()
print(symb*width)
for i in range (height-2):
    print(symb, " "*(width-2), symb, sep="")
print(symb*width)
