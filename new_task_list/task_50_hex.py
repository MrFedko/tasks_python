# # Недавно мы считали для каждого слова количество его вхождений в строку. Но на все слова может быть не так интересно смотреть, как, например, на наиболее часто используемые.
# Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось. Если таких слов несколько, вывести лексикографически первое (можно использовать оператор < для строк).
# В качестве ответа укажите вывод программы, а не саму программу.
# Слова, написанные в разных регистрах, считаются одинаковыми.

# Sample Input: abc a bCd bC AbC BC BCD bcd ABC
# Sample Output: abc 3

text_file = open("dataset_3363_3.txt", 'r')
text = text_file.read().replace('\n', ' ').lower().split()
text_file.close()

def finder_dict(any_text):
    my_dict = {}
    for i in any_text:
        if i not in my_dict:
            my_dict[i] = 1
        elif i in my_dict:
            my_dict[i] += 1
    return my_dict

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k
        
result = finder_dict(text)
print(get_key(result, max(result.values())) ,max(result.values()))