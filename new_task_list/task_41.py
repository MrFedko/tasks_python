# Написать программу вычисления арифметического выражения заданного строкой. Используются операции +,-,/,*. приоритет операций стандартный. 
# Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -6; 

my_string = '11+2*3*(3+4)'

print(eval(my_string, {'__builtins__': None}))

# def calculator(any_string):
#     new_list = []
#     # my_set = set('0123456789')
#     my_set_commands = set('(+-/*)')
#     number = ''
#     for i in range(len(any_string)):
#         number += any_string[i]
        
#         if (i+1) >= len(any_string) and any_string[i] in my_set_commands:
#             new_list.append(any_string[i])
#             number = ''
#         elif any_string[i] in my_set_commands and any_string[i+1] in my_set_commands or any_string[i] in my_set_commands:
#             new_list.append(any_string[i])
#             number = ''
#         elif (i+1) >= len(any_string) or any_string[i + 1] in my_set_commands:
#             new_list.append(int(number))
#             number = ''
#     return new_list
# my_list = calculator(my_string)
# print(my_list)