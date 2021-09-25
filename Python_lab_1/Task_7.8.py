count = int(input())
k=0
while(count):
    string = input()
    if string == "раз":
        k+=1
        string = input()
        if string == "два":
            k+=1
            string = input()
            if string == "три":
                k+=1
                string = input()
                if string == "четыре":
                    k+=1
                else:
                    print("Правильных отсчётов было ",k,", но теперь вы ошиблись.", sep="")
                    k=0
                    count-=1
                    continue
            else:
                print("Правильных отсчётов было ",k,", но теперь вы ошиблись.", sep="")
                k=0
                count-=1
                continue
        else:
            print("Правильных отсчётов было ",k,", но теперь вы ошиблись.", sep="")
            k=0
            count-=1
            continue
    else:
        print("Правильных отсчётов было ",k,", но теперь вы ошиблись.", sep="")
        k=0
        count-=1
        continue
print("На сегодня хватит.")
        
    
