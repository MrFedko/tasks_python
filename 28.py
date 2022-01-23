# Подсчитать сумму цифр в числе

import random
num = random.randint(300, 9999)
print(num)

def how_much_digits(number):
    result = 0
    while number != 0:
        result += number % 10
        number //= 10
    return result
    
print(how_much_digits(num))