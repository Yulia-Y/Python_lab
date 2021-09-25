count_move = 0
treasure_is_found = False
treasure_x = int(input())
treasure_y = int(input())
x = 0
y = 0
look_at = 'север'
move = ''
while move != 'стоп':
    if int(treasure_x) == x and int(treasure_y) == y and not treasure_is_found:
        min_count_move = count_move
        look_at_treasure = look_at
        treasure_is_found = True
    else:
        move = input()
        count_move += 1
        if move == 'вперёд':
            steps = int(input())
            if look_at == 'север':
                y += steps
            elif look_at == 'запад':
                x -= steps
            elif look_at == 'юг':
                y -= steps
            elif look_at == 'восток':
                x += steps
        elif move == 'направо':
            if look_at == 'север':
                look_at = 'восток'
            elif look_at == 'восток':
                look_at = 'юг'
            elif look_at == 'юг':
                look_at = 'запад'
            elif look_at == 'запад':
                look_at = 'север'
        elif move == 'налево':
            if look_at == 'север':
                look_at = 'запад'
            elif look_at == 'запад':
                look_at = 'юг'
            elif look_at == 'юг':
                look_at = 'восток'
            elif look_at == 'восток':
                look_at = 'север'
        elif move == 'разворот':
            if look_at == 'север':
                look_at = 'юг'
            elif look_at == 'юг':
                look_at = 'север'
            elif look_at == 'запад':
                look_at = 'восток'
            elif look_at == 'восток':
                look_at = 'запад'
print(min_count_move)
print(look_at_treasure)