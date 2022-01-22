# Написать программу преобразования десятичного числа в двоичное

number = int(input('введите число для преобразования в двоичное: '))

def double_calc(n):
    result = ''
    while n != 0:
        result = str(n % 2) + result
        n //= 2
    return result

result = double_calc(number)
print(result)