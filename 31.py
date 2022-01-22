# Задать массив из 8 элементов и вывести их на экран

import random
array = []
for i in range(1, 9):
    array.append(random.randint(1, 999))
    
print(array)