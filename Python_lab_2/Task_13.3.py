res = [0]
for _ in range(int(input())):
  res.append(sum((x == y for x,y in zip(res,reversed(res)))))
print(*res,sep ='\n')