# Задать список из n чисел последовательности (1+1/n)**n и вывести на экран их сумму

n = int(input('Введите сколько чисел последовательности вывести на экран: '))

def sequence(number):
    my_list = []
    for i in range(1, number):
        my_list.append((1 + 1/i) ** i)
    return my_list

print(*sequence(n))
print(sum(sequence(n)))