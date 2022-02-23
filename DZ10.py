while True:
    s = input("Выберите действие('+','-','*','/')"
              "\nпродолжить работу ('yes')закончить ('no')")
    if s == 'no':
        print("END")
        print('-' * 30)
        break
    if s in ('+','-','*','/'):
        a = float(input("Ввидите число"))
        b = float(input("Ввидите число"))
        if s == '+':
            c = a + b
            print("Результат" + str(c))
            print("END")
            print ('-' * 30)
        elif s == '-':
            c = a - b
            print("Результат"+ str(c))
            print("END")
            print('-' * 30)
        elif s == '*':
            c = a * b
            print("Результат"+ str(c))
            print("END")
            print('-' * 30)
        elif s == '/':
            if b:
                c = a / b
                print("Результат" + str(c))
                print("END")
                print('-' * 30)
            else:
                print("Деление на ноль не возможно!")
                print( '-' * 30)























