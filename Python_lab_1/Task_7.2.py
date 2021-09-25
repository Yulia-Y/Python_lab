flag = True
index = -1
k=0
while flag:
    string = input()
    k+=1
    if index==-1 and ("Кот" in string or "кот" in string) :
        index = k
    elif string == "СТОП":
        flag = False
print(index)
    
        