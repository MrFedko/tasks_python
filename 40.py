# В Указанном массиве вещественных чисел найдите разницу между максимальным и минимальным элементом

import random
array = []

for i in range(0, 11):
    array.append(random.randint(1, 9999))
    
min_value = min(array)
max_value = max(array)

print(f'{array} \n {max_value} - {min_value} = {max_value - min_value}')