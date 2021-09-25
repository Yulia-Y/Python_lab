password = input()
password2 = input()
if len(password)<8:
    print("Короткий!")
elif "123" in password :
    print("Простой!")
elif password!=password2:
    print("Различаются!")
else:
    print("OK")
    
    