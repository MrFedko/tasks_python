## Выяснить является ли число чётным

import random
num = random.randint(1,9999)

if num % 2 == 0:
    print(f'число {num} является четным')
else:
    print(f'число {num} не является четным')