# Подсчитать сумму цифр в вещественном числе.

n = input('Введите вещественное число: ')
summa = sum(list(map(int, n.replace('.', '0'))))
print(summa)
