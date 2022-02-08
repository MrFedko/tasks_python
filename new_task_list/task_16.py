# Задать список из n чисел последовательности (1+1/n)**n и вывести на экран их сумму

from itertools import accumulate

n = int(input('Введите сколько чисел последовательности вывести на экран: '))

def sequence(number):
    my_list = []
    for i in range(1, number + 1):
        my_list.append((1 + 1/i) ** i)
    return my_list

my_func = lambda _, x: ((1 + 1/x) ** x)
my_list = list(accumulate([x for x in range(1, n + 1)], my_func, initial = 1))
my_list = my_list[1:]

print(*sequence(n))
print(sum(sequence(n)))
print(*my_list)
print(sum(my_list))