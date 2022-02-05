# Sample Input:
# Петров;85;92;78
# Сидоров;100;88;94
# Иванов;58;72;85

# Sample Output
# 85.0
# 94.0
# 71.666666667
# 81.0 84.0 85.666666667

from re import A


spisok = []
with open('dataset_3363_4.txt') as file:
    for line in file:
        line = line.strip()
        spisok.append(line.split(';'))
[print(i) for i in spisok]

a, b, c = 0, 0, 0
for el in spisok:
    a += int(el[1])
    b += int(el[2])
    c += int(el[3])
a /= len(spisok)
b /= len(spisok)
c /= len(spisok)

with open('task_51_result.txt', 'w') as file:
    file.writelines((str((int(priceLow) + int(priceHigh) + int(c)) / 3)+'\n') for fruit, priceLow, priceHigh, c in spisok)
    file.write(f'{a} {b} {c}')
    