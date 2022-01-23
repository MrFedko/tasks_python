# Определить количество цифр в числе

num = int(input('введите число: '))

def how_long_number(number):
    count = 0
    while number != 0:
        number //= 10
        count += 1
    return count
    
print(how_long_number(num))