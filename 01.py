## По двум заданным числам проверять является ли первое квадратом второго
num = int(input())
num2 = int(input())

if num ** 0.5 == num2:
    print(f'{num} является квадратом {num2}')
else:
    print(f'{num} не является квадратом {num2}')