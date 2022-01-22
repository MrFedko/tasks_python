# Найти произведение пар чисел в одномерном массиве. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random
array = []
new_array = []
my_summa = 0

for i in range(0, 11):
    array.append(random.randint(1, 9))
 
print(array)
   
   
if len(array) % 2 != 0:
    for i in range(0, round((len(array) - 1) / 2)):
        new_array.append(array[i] * array[(i + 1) * (-1)])
    new_array.append(array[round((len(array) - 1 )/ 2)])
else:
    for i in range(0, round(len(array) / 2)):
        new_array.append(array[i] * array[(i + 1) * (-1)])
    
print(new_array)