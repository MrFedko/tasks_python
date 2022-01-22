# Найти сумму чисел одномерного массива стоящих на нечетной позиции

import random
array = []
my_summa = 0

for i in range(1, 15):
    array.append(random.randint(1, 9))
    
for i in range(1, len(array), 2):
    my_summa += array[i]
    
print(array, my_summa)