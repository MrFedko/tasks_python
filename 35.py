# Определить, присутствует ли в заданном массиве, некоторое число

import random
array = []
for i in range(1, 9):
    array.append(random.randint(1, 10))
print(array)   
num = int(input('введите число которое будем искать: '))


if num in array:
    print(f'да, оно есть на позиции {array.index(num) + 1}. всего в списке это число встречается {array.count(num)} раз(а)')
else:
    print('такого числа нет')
