# Задать двумерный массив следующим правилом: Aₘₙ = m+n
m = int(input('Введите число m: '))
n = int(input('Введите число n: '))
array = [[0 for i in range(0, m)] for j in range(0, n)]

for i in range(0, m):
    for j in range(0, n):
        array[j][i] = i + j
        
for i in array:
    print(i)