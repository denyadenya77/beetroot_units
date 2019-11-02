# Создать иерархию наследования классов: Человек, Мужчина, Женщина,
# Супермен (с приватным атрибутом force и методом save_world)

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Man(Person):

    def __init__(self, name, age, beard):
        super().__init__(name, age)
        self.bread = beard


class Woman(Person):

    def __init__(self, name, age, hair_color):
        super().__init__(name, age)
        self.hair_color = hair_color


class Superhero(Person):

    def __init__(self, name, age, force):
        super().__init__(name, age)
        self.force = force

    def save_world(self):
        return f'{self.name} saved the world with {self.force}'