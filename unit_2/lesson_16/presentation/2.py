# Создать класс Солдат. Добавить экземпляры класса Солдат в класс Армия. Создать итератор для солдат в Армии.


class Soldier:

    def __init__(self, name):
        self.name = name


class Army:

    def __init__(self, *args):
        self.soldiers = [x for x in args]


class Army_iter:

    def __init__(self, army):
        self.army = army
        self.iter_index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.iter_index += 1
        if self.iter_index < len(self.army.soldiers):
            return self.army.soldiers[self.iter_index].name
        else:
            raise StopIteration


s1 = Soldier('Denys')
s2 = Soldier('Alex')
s3 = Soldier('Misha')

a1 = Army(s1, s2, s3)

a1_iter = Army_iter(a1)

print(next(a1_iter))
print(next(a1_iter))
print(next(a1_iter))
print(next(a1_iter))
