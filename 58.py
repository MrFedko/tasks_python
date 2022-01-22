# Написать программу, которая в двумерном массиве заменяет строки на столбцы или сообщить, 
# что это невозможно (в случае, если матрица не квадратная).

import random


m = int(input('Введите число m: '))
n = int(input('Введите число n: '))
array = [[0 for i in range(0, m)] for j in range(0, n)]
if m != n:
    print('замена не возможна!')
    exit(0)

def fill(any):
    for i in range(0, len(any)):
        for j in range(0, len(any[0])):
            any[j][i] = random.randint(1, 9)
    return any

def print_ar(any):
    for i in any:
        print(i)  

def rebase(any):
    new_any = [[0 for i in range(0, len(any))] for j in range(0, len(any))]
    for i in range(0, len(any)):
        for j in range(0, len(any[0])):
            new_any[j][i] = any[i][j]
    return new_any
        
fill(array)
print_ar(array)
print()
print_ar(rebase(array))