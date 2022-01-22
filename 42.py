# Определить сколько чисел больше 0 введено с клавиатуры

count = 0

while True:
    my_number = input()
    if my_number == 'end':
        break
    if int(my_number) > 0:
        count += 1
print(count)