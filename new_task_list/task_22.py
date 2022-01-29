# Найти сумму чисел списка стоящих на нечетной позиции

import random

def fill(any):
    new_list = []
    for i in range(any):
            new_list.append(random.randint(1, 9))
    return new_list

def summ_odd(any_list):
    summa = 0
    for i in range(1, len(any_list), 2):
        summa += any_list[i]
    return summa

my_list = fill(10)
print(my_list, summ_odd(my_list))
