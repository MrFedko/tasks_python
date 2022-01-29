# Реализовать алгоритм перемешивания списка. 

import random

def fill(any):
    new_list = []
    for i in range(any):
            new_list.append(random.randint(1, 99))
    return new_list

def randomizer(any):     
    for i in range(round(len(any) / 2) , len(any)):
        j = len(any) - i
        any[i], any[j] = any[j], any[i]
    return any

my_list = fill(10)
print(*my_list)
random.shuffle(my_list)
print(*my_list)
print(*randomizer(my_list))