# Строка содержит набор чисел. Показать большее и меньшее число

my_string = [float(x) for x in input('введите числа через пробел: ').split()]

print(my_string)
print(min(my_string), max(my_string))