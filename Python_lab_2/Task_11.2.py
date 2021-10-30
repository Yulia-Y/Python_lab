a = []
for i in range(int(input())):
    a.append(input())
for i in a:
    if i[0:4] != '####':
        if i[0:2] == '%%': 
            print(i[2:])
        else: 
            print(i)