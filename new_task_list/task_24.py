# В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов. 
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

def fill(any):
    new_list = []
    for i in range(any):
            new_list.append(round(random.uniform(1, 9), 2))
    return new_list

def difference(any_list):
    for i in range(len(any_list)):
        any_list[i] = any_list[i] % 1
    return round(max(any_list) - min(any_list),2)

my_list = fill(10)
print(*my_list)
print(difference(my_list))