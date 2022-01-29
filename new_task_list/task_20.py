# Определить, присутствует ли в заданном списке строк, некоторое число

my_string = ['sfd3', 'sdfeq5', '13', 'sd831sd']
n = int(input('какое число разыскиваем? '))
n = str(n)

def search(any, number):
    count = 0
    for i in any:
        if number in i:
            return True
    if count == 0:
        return False

print(search(my_string, n))