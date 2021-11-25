import random

st1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'p', 'a', 's', 'd', 'f', 'g', 
       'h', 'j', 'k', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
st2 = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 
       'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
st3 = ['2', '3', '4', '5', '6', '7', '8', '9']
st4 = st1 + st2 + st3
 
 
def generate_password(m):
    pas = []
    pas.append(random.choice(st1))
    pas.append(random.choice(st2))
    pas.append(random.choice(st3))
    for i in range(0, m - 3):
        pas.append(random.choice(st4))
    random.shuffle(pas)
    return ''.join(pas)
 
 
def main(n, m):
    list_passw = set()
    while len(list_passw) < n:
        list_passw.add(generate_password(m))
    return list_passw
print("Случайный пароль из 7 символов:", generate_password(7))  
print("10 случайных паролей длиной 15 символов:")  
print(*main(10, 15), sep="\n")