flag = True
index = -1
k=0
count = 0
while flag:
    string = input()
    k+=1
    if "Кот" in string or "кот" in string:
        if index == -1:
            index = k
        count+=1
    elif string == "СТОП":
        flag = False
print(count, index)