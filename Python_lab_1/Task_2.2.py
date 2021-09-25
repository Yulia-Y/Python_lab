login=input()
address=input()
if '@' in login:
    print("Некорректный логин")
elif'@' not in address:
    print("Некорректный адрес")
else:
    print("OK")