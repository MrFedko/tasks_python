# Для натурального N создать список: 1, -3, 9, -27, 81 и т.д.

n = int(input('Введите сколько чисел последовательности вывести на экран: '))

def sequence(number):
    my_list = [1, ]
    for i in range(number + 1):
        my_list.append(-3**i)
    return my_list
print(*sequence(n))