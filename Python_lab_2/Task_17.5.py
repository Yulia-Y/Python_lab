ways = [input() for i in range(int(input()))]
files = [input() for i in range(int(input()))]
 
lst_ways = [x.split('/')[1:] for x in ways]
lst_files = [x.split('/')[1:] for x in files]
 
 
def check_permissions(ways, file):
    for x in ways:
        if len(file) < len(x):
            continue
        else:
            if x == file[:len(x)]:
                return 'YES'
    return 'NO'
 
 
for i in lst_files:
    print(check_permissions(lst_ways, i))