# Подсчитать сумму цифр в вещественном числе.

def summ_of_float(number):
    summa = 0
    number = number.replace('.', '0')
    for i in range(len(number)):
        summa += int(number[i])
    return summa

def is_number(str):
    try:
        float(str)
        return summ_of_float(str)
    except ValueError:
        return False

n = input('Введите вещественное число: ')
print(is_number(n))
    