# memo = hashmap
# Function F(integer i):
#     if i is 0 or 1: 
#         return i
#     if i doesn't exist in memo:
#         memo[i] = F(i - 1) + F(i - 2)
#     return memo[i]

memo_fibo = {1: 0, 2: 1}

def fibo(number):
    if number in range(0, 1):
        return number
    if number not in memo_fibo:
        memo_fibo[number] = fibo(number - 1) + fibo(number - 2)
    return memo_fibo[number]
    
fibo(100)
print(memo_fibo)