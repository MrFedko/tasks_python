# Задать массив, заполнить случайными положительными трёхзначными числами. Показать количество нечетных\четных чисел

import random
array = []
count_even = 0

for i in range(1, 9):
    array.append(random.randint(100, 999))
print(array)  

for i in array:
    if i % 2 == 0:
        count_even += 1
        
print(f'четных чисел {count_even}, а нечетных {len(array) - count_even}')