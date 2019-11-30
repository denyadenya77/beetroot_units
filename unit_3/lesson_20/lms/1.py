# Memoization

from functools import lru_cache


# f_cache = {}


# def fibonacci(n):
#     if n in f_cache:
#         return f_cache[n]
#     if n == 1:
#         value = 1
#     elif n == 2:
#         value = 1
#     elif n > 2:
#         value = fibonacci(n - 1) + fibonacci(n - 2)
#     f_cache[n] = value
#     return value
#
#
# for n in range(1, 501):
#     print(f'{n} : {fibonacci(n)}')



@lru_cache(maxsize=1000)
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n - 1) + fibonacci(n - 2)


for n in range(1, 1001):
    print(f'{n} : {fibonacci(n)}')
