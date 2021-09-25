flag = True
k=0
while flag:
    string = input()
    k+=1
    if "Кот" in string or "кот" in string :
        print(k)
        break
    elif string == "СТОП":
        flag = False
        print(-1)
