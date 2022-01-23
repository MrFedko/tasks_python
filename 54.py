# В матрице чисел найти сумму элементов главной диагонали

import random
from all_def import fill, print_ar
m = int(input('Введите число m: '))
array = [[0 for i in range(0, m)] for j in range(0, m)]

def summa(any):
    j = 0
    summ = 0
    for i in range(0, len(any)):
        summ += any[i][j]
        j += 1
    return summ
      

fill(array)
print_ar(array)
print(summa(array))