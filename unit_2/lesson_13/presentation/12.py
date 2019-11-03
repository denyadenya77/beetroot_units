# С помощью функции map преобразовать список с милями в список с километрами, где 1 mile = 1.6 km.

l_miles = [10, 15, 246]
l_km = list(map(lambda x: x * 1.6, l_miles))
print(l_km)
