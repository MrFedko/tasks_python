# В матрице чисел найти сумму элементов главной диагонали

import random
m = int(input('Введите число m: '))
array = [[0 for i in range(0, m)] for j in range(0, m)]

def fill(any):
    for i in range(0, len(any)):
        for j in range(0, len(any[0])):
            any[j][i] = random.randint(1, 9)
    return any

def summa(any):
    j = 0
    summ = 0
    for i in range(0, len(any)):
        summ += any[i][j]
        j += 1
    return summ

def print_ar(any):
    for i in any:
        print(i)          

fill(array)
print_ar(array)
print(summa(array))