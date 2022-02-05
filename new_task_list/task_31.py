# Составить список простых множителей натурального числа N

n = int(input('введите число: '))

def is_prime(number):
    divider = 2
    while number % divider != 0:
        divider += 1
    return divider == number

def search_multipliers(number):
    multipliers = []
    divider = 2
    while divider * divider <= number:
        if number % divider == 0:
            multipliers.append(divider)
            number //= divider
        else:
            divider += 1
    if number > 1:
        multipliers.append(number)   
    return multipliers

if is_prime(n) == True: 
    print('Это простое число и у него 1 множитель/делитель')
else:
    print(search_multipliers(n))