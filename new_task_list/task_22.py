# Найти сумму чисел списка стоящих на нечетной позиции

import random

def fill(any):
    return [random.randint(1,9) for x in range(any)]

def summ_odd(any_list):
    return sum(any_list[1::2])

my_list = fill(10)
print(my_list, summ_odd(my_list))
