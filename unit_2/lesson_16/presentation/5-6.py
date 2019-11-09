# Написать генератор который будет выдавать все простые числа до n.
# Написать генератор для генерации бесконечного ряда простых чисел.
import math, sys


def gen_primes():

    for num in range(3, sys.maxsize, 2):
        if all(num % i != 0 for i in range(3, int(math.sqrt(num)) + 1, 2)):
            yield num

a = gen_primes()
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))