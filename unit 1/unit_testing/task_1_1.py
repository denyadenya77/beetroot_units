# Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-е простое число - 13.
# Какое число является 10001-м простым числом?
import math, sys


a = [2]
print(a[-1])
# записываем все результаты в список
while len(a) <= 10001:
    for num in range(3, sys.maxsize, 2):
        if all(num % i != 0 for i in range(3, int(math.sqrt(num)) + 1, 2)):
            a.append(num)
            print(num)
