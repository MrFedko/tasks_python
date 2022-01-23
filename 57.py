# Написать программу, упорядочивания по убыванию элементы каждой строки двумерной массива.

import random
from all_def import fill, print_ar

m = 4
array = [[0 for i in range(0, m)] for j in range(0, m)]
        
def sorting(any):
    for i in any:
        i.sort(reverse = True)
    return any

fill(array)
print_ar(array)
print()
sorting(array)
print_ar(array)