## Дано число. Проверить кратно ли оно 7 и 23

import random
num = random.randint(1, 10000)

if num % 7 == 0 and num % 23 == 0:
    print(f'число {num} кратно 7 и 23')
else:
    print(f'число {num} не кратно 7 и 23')