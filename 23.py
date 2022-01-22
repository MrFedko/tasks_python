# Показать таблицу квадратов чисел от 1 до N

import random
num = random.randint(1, 99)
for i in range(1, num):
    print(f'{i} ^ 2 = {i ** 2}')