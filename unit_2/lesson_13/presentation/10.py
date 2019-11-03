# С помощью функции reduce умножить все числа в списке.

from functools import reduce

l = [2, 5, 7, 12, 34]

ll = reduce(lambda x, y: x * y, l)
print(ll)