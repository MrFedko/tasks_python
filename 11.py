# Дано число из отрезка [10, 99]. Показать наибольшую цифру числа
import random
num = random.randint(10, 99)
first_num = num % 10
second_num = num // 10

print(f'{num} {max(first_num, second_num)}')