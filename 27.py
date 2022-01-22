# Определить количество цифр в числе

num = int(input('введите число: '))

count = 0

while num != 0:
    num //= 10
    count += 1
    
print(count)