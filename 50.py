# В двумерном массиве n×k заменить четные элементы на противоположные
import random


m = int(input('Введите число m: '))
n = int(input('Введите число n: '))
array = [[0 for i in range(0, m)] for j in range(0, n)]

for i in range(0, m):
    for j in range(0, n):
        array[j][i] = random.randint(1, 99)

for i in range(0, m):
    for j in range(0, n):
        if array[j][i] % 2 == 0:
            array[j][i] *= -1
        
for i in array:
    print(i)