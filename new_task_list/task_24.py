# В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов. 
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

def fill(any):
    return [round(random.uniform(1,9), 2) for x in range(any)]

def difference(any_list):
    any_list = list(map(lambda x: x % 1, any_list))
    return round(max(any_list) - min(any_list),2)

my_list = fill(10)
print(*my_list)
print(difference(my_list))