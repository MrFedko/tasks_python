# Задать номер четверти, показать диапазоны для возможных координат

diapason = {1: 'x > 0, y > 0',
            2: 'x < 0, y > 0',
            3: 'x < 0, y < 0',
            4: 'x >0, y < 0'}

num = int(input('введите номер четверти '))

if num in diapason:
    print(diapason[num])