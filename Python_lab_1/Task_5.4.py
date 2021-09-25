Pile = int(input())
print("В куче", Pile ,"камней")
while Pile!=0:
    if Pile <=3:
        print("Взято",Pile, "камней")
        Pile = 0
    elif Pile%3==1:
        print("Взято 3 камня")
        Pile -= 3
    elif Pile%3 == 2:
        print("Взят 1 камень")
        Pile -= 1
    else:
        print("Взято 2 камня")
        Pile -= 2
    print("В куче", Pile ,"камней")
    if Pile == 0:
        print("Победил компьютер")
        break
    count = int(input())
    while count>3 or count > Pile:
        count = int(input())
    print("Взято", count , "камней")
    Pile -= count
    print("В куче", Pile ,"камней")
    if Pile == 0:
        print("Вы победили!")
        