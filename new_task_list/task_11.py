# Для натурального N создать список: 1, -3, 9, -27, 81 и т.д.

n = int(input('Введите сколько чисел последовательности вывести на экран: '))

def sequence(number):
    my_list = [1, ]
    for i in range(1, number):
        if my_list[i - 1] > 0:
            my_list.append(-3**i)
        else:
            my_list.append(3**i)
    return my_list

print(*sequence(n))