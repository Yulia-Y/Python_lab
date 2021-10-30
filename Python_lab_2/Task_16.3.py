n = int(input())
field = []
for i in range(n):
    field.append([0] * n)
for a in range(n):
    for b in range(n):
        field[a][b] = int(input())
k = int(input())
for j in range(k):
    y = int(input())
    x = int(input())
    field[x][y] -= 8
    if x - 1 >= 0 and y - 1 >= 0:
        field[x - 1][y - 1] -= 4
    if x - 1 >= 0:
        field[x - 1][y] -= 4
    if y - 1 >= 0:
        field[x][y - 1] -= 4
    if x + 1 < n and y + 1 < n:
        field[x + 1][y + 1] -= 4
    if x + 1 < n:
        field[x + 1][y] -= 4
    if y + 1 < n:
        field[x][y + 1] -= 4
    if x - 1 >= 0 and y + 1 < n:
        field[x - 1][y + 1] -= 4
    if x + 1 < n and y - 1 >= 0:
        field[x + 1][y - 1] -= 4
for c in range(n):
    for d in range(n):
        if field[c][d] < 0:
            field[c][d] = 0
for i in range(n):
    field[i] = ' '.join(str(v) for v in field[i])
print('\n'.join(field))