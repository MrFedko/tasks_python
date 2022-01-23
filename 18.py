# # Проверить истинность утверждения ¬(X ⋁ Y) = ¬X ⋀ ¬Y

def TrueFalse(x, y):
    FlagX = bool(x != 0)
    FlagY = bool(y != 0)
    left = not(FlagX or FlagY)
    right = not FlagX and not FlagY
    return left == right

for i in range(0,2):
    for j in range(0,2):
        if TrueFalse(i, j):
            print(f'При x = {i} и y = {j} выражение ¬(X ⋁ Y) = ¬X ⋀ ¬Y истинно')
        else:
            print(f'При x = {i} и y = {j} выражение ¬(X ⋁ Y) = ¬X ⋀ ¬Y ложно')
        j += 1
    i += 1
