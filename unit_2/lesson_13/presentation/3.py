# Объявить две функции: 1 - принимает список чисел как аргумент и сортирует его по убыванию,
# 2 - принимает список чисел как аргумент и сортирует его по возрастанию. Отсортировать список
# чисел по убыванию или по возрастанию, в зависимости от того что выберет пользователь.
# Реализовать с помощью функции, которая передается как аргумент.

import random


def increase_sort(a):
    return sorted(a)


def decrease_sort(a):
    a.sort()
    a.reverse()
    return a


def your_choice(a, b):
    print(b(a))


a = random.sample(range(100), 10)
print(a)

your_choice(a, increase_sort)
your_choice(a, decrease_sort)