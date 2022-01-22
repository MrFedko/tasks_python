# Программа проверяет пятизначное число на палиндромом.
num = int(input('введите пятизначное число '))

def palindrom(x):
    if x % 10 == x // 10000 and (x % 100)//10 == (x // 1000) % 10:
        return True

if palindrom(num):
    print(f'{num} является палиндромом')
else:
     print(f'{num} не является палиндромом')
