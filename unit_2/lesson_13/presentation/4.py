# Написать функцию таймер, которая будет принимать функцию как аргумент и вычислять время выполнения этой функции.
import timeit


def the_sum(a=5, b=5):
    return a + b


def speed(func):
    c = timeit.Timer(func).repeat(1)
    return c


x = speed(the_sum)
print(x)
