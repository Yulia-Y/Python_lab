while True:
    number = int(input())
    operation = input()
    if operation == '+':
        number+=int(input())
    elif operation == '-':
        number-=int(input())
    elif operation == '*':
        number*=int(input())
    elif operation == '/':
        x=int(input())
        if x!=0:
            number//=x
    elif operation == '%':
        x=int(input())
        if x!=0:
            number%=x
    elif operation == '!':
        if number>=0:
            factorial = 1
            while number > 1:
                factorial *= number
                number -= 1
            number = factorial
    elif operation == 'x':
        print(number)
        break
    print(number)    
        
