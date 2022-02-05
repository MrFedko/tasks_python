# В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его. [5, 7, 8, 9]
file = open('file_35.txt', 'r')
my_list = [int(i) for i in file.readline().split()]
file.close()

def find_number(any_list):
    for i in range(1, len(any_list)):
        if any_list[i] - 1 != any_list[i - 1]:
            return any_list[i - 1] + 1

print(find_number(my_list))        