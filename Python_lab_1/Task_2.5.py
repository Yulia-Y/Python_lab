print("Какое ваше любимое время года?")
choice = input()
if choice == 'зима':
    print("Вам больше нравится день или ночь?")
    choice = input()
    if choice == 'день':
        print("Вы очень открытая личность")
    elif choice == 'ночь':
        print("Вы холодная личность")
    else:
        print("ERROR")
elif choice == 'весна':
    print("Вам больше нравится день или ночь?")
    choice = input()
    if choice == 'день':
        print("У вас очень молодая душа")
    elif choice == 'ночь':
        print("Вы очень мудры")
    else:
        print("ERROR")
elif choice == 'лето':
    print("Вам больше нравится день или ночь?")
    choice = input()
    if choice == 'день':
        print("Вы очень доброжелательны к окружающим")
    elif choice == 'ночь':
        print("Вы живете на полную катушку")
    else:
        print("ERROR")  
elif choice == 'осень':
    print("Вам больше нравится день или ночь?")
    choice = input()
    if choice == 'день':
        print("Вы весьма утонченная натура")
    elif choice == 'ночь':
        print("В душе вы романтик")
    else:
        print("ERROR")
else:
    print("ERROR")