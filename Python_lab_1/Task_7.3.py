count = int(input())
for i in range (count):
    string = input()
    if "Кот" in string or "кот" in string:
        print("МЯУ")
        break
    if i == count-1:
        print("НЕТ")