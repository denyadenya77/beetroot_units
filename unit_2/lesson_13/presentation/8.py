# С помощью функции map преобразовать случайного список целых чисел в новый список где каждый елеменет
# будет умножен на 2.

import random


def mult(x):
    return x * 2


l = random.sample(range(100), 10)
print(l)
ll = list(map(mult, l))
print(ll)
