# Найти произведение двух матриц

import random
from all_def import fill, print_ar

m = 5
array = [[0 for i in range(0, m)] for j in range(0, m)]
array2 = [[0 for i in range(0, m)] for j in range(0, m)]

def product(any, any2):
    new_any = [[0 for i in range(0, len(any))] for j in range(0, len(any))]
    for i in range(0, len(any)):
        for j in range(0, len(any[0])):
            new_any[i][j] = any[i][j] * any2[i][j]
    return new_any

fill(array)
fill(array2)
print_ar(array)
print()
print_ar(array2)
print()
print_ar(product(array, array2))