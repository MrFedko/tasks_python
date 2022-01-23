# Дан целочисленный массив. Найти среднее арифметическое каждого из столбцов.

import random
from all_def import fill, print_ar

m = 4
array = [[0 for i in range(0, m)] for j in range(0, m)]
       
def middle(any):
    mid = []
    summ = 0
    for i in range(0, len(any)):
        for j in range(0, len(any[0])):
            summ += any[j][i]
        mid.append(summ/len(any))
        summ = 0
    return mid
            
fill(array)
print_ar(array)
print(middle(array))