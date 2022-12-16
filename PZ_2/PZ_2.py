import threading

print('Заданные числа: 7 и 3')
print('Будут рассчитаны сумма, разность, произведение и частное данных чисел\n')

def sum(a, b):
        sum1 = a + b
        with open('sum.txt', 'w+', encoding='utf-8')as file:
            file.write(f'Результат сложения: {sum1}\n')
            print(f'Результат сложения: {sum1}\n')

def div(a, b):
    div1 = a / b
    with open('division.txt', 'w+', encoding='utf-8') as file:
        file.write(f'Результат деления: {div1}\n')
        print(f'Результат деления: {div1}\n')

def mul(a, b):
    mul1 = a * b
    with open('multiplication.txt', 'w+', encoding='utf-8') as file:
        file.write(f'Результат умножения: {mul1}\n')
        print(f'Результат умножения: {mul1}\n')

def sub(a, b):
        sub1 = a - b
        with open('subtraction.txt', 'w+', encoding='utf-8') as file:
            file.write(f'Результат вычитания: {sub1}\n')
            print(f'Результат вычитания: {sub1}\n')

with open('Result.txt', 'w+', encoding='windows-1251') as fil:
    f1 = open('sum.txt', 'r')
    f2 = open('multiplication.txt', 'r')
    f3 = open('subtraction.txt', 'r')
    f4 = open('division.txt', 'r')
    print(f1.read(), '\n', f2.read(), '\n', f3.read(), '\n', f4.read(), '\n', file=fil)

e1 = threading.Event()
e2 = threading.Event()
e3 = threading.Event()
e4 = threading.Event()

t1 = threading.Thread(target=sum, args=(7, 3))
t2 = threading.Thread(target=mul, args=(7, 3))
t3 = threading.Thread(target=sub, args=(7, 3))
t4 = threading.Thread(target=div, args=(7, 3))

t1.start()
t2.start()
t3.start()
t4.start()

e1.set()

t1.join()
t2.join()
t3.join()
t4.join()