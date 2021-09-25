money = int(input())
count = int(input())
count_bull = 1
count_calf = (money-20)//5
if (count_calf + count_bull) > count:
    count_cow = count_calf + count_bull - count
    count_calf -= count_cow*2
else:
    count_cow = 0
print(count_bull, count_cow, count_calf)
while(count_cow >= 3):
    count_cow-=3
    count_bull+=1
    count_calf+=2
    print(count_bull, count_cow, count_calf)

