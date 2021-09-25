Pile_1 = int(input())
Pile_2 = int(input())
Pile_3 = int(input())
while Pile_1 != 0 or Pile_2 != 0 or Pile_3 != 0:
    Pile = int(input())
    count = int(input())
    if Pile == 1:
        Pile_1 -= count
    elif Pile == 2:
        Pile_2 -= count
    else:
        Pile_3 -= count
    print(Pile_1, Pile_2, Pile_3)