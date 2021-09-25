Pile = int(input())
print("В куче", Pile ,"камней")
while Pile!=0:
    if 1<Pile<=4:
        print("Взято",Pile-1, "камней")
        Pile = 1
    else:
        print("Взят 1 камень")
        Pile -= 1
    print("В куче", Pile ,"камней")
    if Pile == 0:
        print("Вы победили!")
        break
    count = int(input())
    while count>3 or count > Pile:
        count = int(input())
    print("Взято", count , "камней")
    Pile -= count
    print("В куче", Pile ,"камней")
    if Pile == 0:
        print("Победил компьютер")
        