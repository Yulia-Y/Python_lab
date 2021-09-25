count_move = 0
treasure_is_found = False
treasure_x = int(input())
treasure_y = int(input())
x = 0
y = 0
move = input()
if treasure_x == 0 and treasure_y == 0:
    print(0)
while move != 'стоп':
    steps = int(input())
    count_move += 1
    if move == 'север':
        y += steps
    elif move == 'запад':
        x -= steps
    elif move == 'юг':
        y -= steps
    elif move == 'восток':
        x += steps
    if int(treasure_x) == x and int(treasure_y) == y and not treasure_is_found:
        min_count_move = count_move
        treasure_is_found = True
    move = input()
print(min_count_move)