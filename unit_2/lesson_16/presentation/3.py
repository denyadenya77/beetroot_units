# Создать генератор для итерации по солдатам.


def generate_soldiers(x):
    army = ['JAMES', 'JOHN', 'ROBERT', 'MICHAEL', 'WILLIAM', 'DAVID', 'RICHARD', 'CHARLES', 'JOSEPH', 'THOMAS']
    a = 0
    while a < x:
        yield f'soldier {army[a]} ready for battle'
        a += 1


my_own_army = generate_soldiers(9)
print(next(my_own_army))
print(next(my_own_army))
print(next(my_own_army))
print(next(my_own_army))
print(next(my_own_army))
print(next(my_own_army))
print(next(my_own_army))
print(next(my_own_army))
print(next(my_own_army))
print(next(my_own_army))
print(next(my_own_army))