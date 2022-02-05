#  Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
#  входные и выходные данные хранятся в отдельных файлах

file = open('dataset_3363_2.txt', 'r')
code = file.readline()
file.close()

def encode(any_string):
    digits = set('0123456789')
    result = ''
    how_long = ''
    char = ''
    for i in range(len(any_string)-1):
        if any_string[i] not in digits:
            char = any_string[i]
        else:
            how_long += any_string[i]
        if any_string[i + 1] not in digits:
            result += str(char) * int(how_long)
            char = ''
            how_long = ''
    return result

result = open('file_42_result.txt', 'w')
result.write(encode(code))
result.close()