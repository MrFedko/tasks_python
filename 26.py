# Возведите число А в натуральную степень B используя цикл

number_a = int(input('введите число А: '))
number_b = int(input('введите целую степень числа А: '))
result = 1
for i in range(1, number_b + 1):
    result *= number_a

print(result)