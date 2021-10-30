flag = False
M = int(input())
arr_M = []
N = int(input())
arr_N = []
for i in range(M):
    arr_M.append(input())
for i in range(N):
    arr_N.append(input())
for i in range(N):
    for j in range(M):
        if arr_M[j]==arr_N[i]:
            flag = True
    if(flag):
        print("YES")
        flag = False
    else:
        print("NO")
    