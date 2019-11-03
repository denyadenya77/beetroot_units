# С помощью функции filter выбрать только положительные целочисленные елементы случайного списка.

import random


l = range(-100, 100)
ll = random.sample(l, 20)
print(ll)

lll = list(filter(lambda x: x > 0, ll))
print(lll)