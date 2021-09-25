flag = False
count = int(input())
for i in range(count):
    string = input()
    if "Кот" in string or "кот" in string:
        flag = True
if flag:
    print("МЯУ")
else:
    print("НЕТ")
    
