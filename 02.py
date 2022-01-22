## Даны два числа. Показать большее и меньшее число

num = int(input())
num2 = int(input())

if num > num2:
    print(f'{num} больше {num2}')
elif num == num2:
    print(f'{num} равно {num2}')
else:
    print(f'{num2} больше {num}')