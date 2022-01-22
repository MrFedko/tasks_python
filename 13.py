# Выяснить, кратно ли число заданному, если нет, вывести остаток.
import random
num = random.randint(1, 999)

num1 = int(input('введите число '))

if num % num1 == 0:
    print(f'число {num} кратно числу {num1}')