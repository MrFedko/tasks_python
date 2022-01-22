# Показать двумерный массив размером m×n заполненный вещественными числами
import random


m = int(input('Введите число m: '))
n = int(input('Введите число n: '))
array = [[0 for i in range(0, m)] for j in range(0, n)]

for i in range(0, m):
    for j in range(0, n):
        array[j][i] = round(random.uniform(1, 99), 4)
        
for i in array:
    print(i)