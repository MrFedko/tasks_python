# В прямоугольной матрице найти строку с наименьшей суммой элементов.

import random
from all_def import fill, print_ar

m = int(input('Введите число m: '))
n = int(input('Введите число n: '))
array = [[0 for i in range(0, m)] for j in range(0, n)]
if m == n:
    print('необходима прямоугольная матрица')
    exit(0)

def search(any):
    min_summa = 99999
    min_list = []
    summ = 0
    for i in any:
        for j in range(0, len(i)):
            summ += i[j]
        if summ < min_summa:
            min_summa = summ
            min_list = i
        summ = 0
    return min_list, min_summa
        

fill(array)
print_ar(array)
print()
print(search(array))