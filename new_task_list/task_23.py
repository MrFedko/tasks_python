# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 

import random

def fill(any):
    return [random.randint(1,9) for x in range(any)]

def product_par(any_list):
    new_list = []
    for i in range(round(len(any_list) / 2)):
        new_list.append(any_list[i] * any_list[-(i+1)])
    return new_list
        
my_list = fill(11)
print(f'{my_list} \n {product_par(my_list)}')

