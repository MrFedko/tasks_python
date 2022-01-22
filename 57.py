# Написать программу, упорядочивания по убыванию элементы каждой строки двумерной массива.

import random
m = 4
array = [[0 for i in range(0, m)] for j in range(0, m)]

def fill(any):
    for i in range(0, len(any)):
        for j in range(0, len(any[0])):
            any[j][i] = random.randint(1, 9)
    return any

def print_ar(any):
    for i in any:
        print(i)  
        
def sorting(any):
    for i in any:
        i.sort(reverse = True)
    return any

fill(array)
print_ar(array)
print()
sorting(array)
print_ar(array)