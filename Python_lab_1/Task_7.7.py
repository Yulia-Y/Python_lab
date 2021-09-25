flag = False
count = int(input())
for i in range(count):
    string = input()
    if ("Кот" in string or "кот" in string) and flag == False:
        flag = True
    if ("Пёс" in string or "пёс" in string) and flag:
        flag = False
if flag:
    print("МЯУ")
else:
    print("НЕТ")