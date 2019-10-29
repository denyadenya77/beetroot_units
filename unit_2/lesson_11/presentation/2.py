# Объявить абстрактный класс Судно с абстрактными методами. Создать иерархию классов: Корабль, Пароход, Катер, Парусник.

from abc import ABC, abstractmethod

class Vessel(ABC):

    distance = 0

    def __init__(self, name, speed, crew):
        self.name = name
        self.speed = speed
        self.crew = crew

    @abstractmethod
    def move(self, new_distance):
        pass

    @abstractmethod
    def __str__(self):
        pass

class Ship(Vessel):

    def __init__(self, name, speed, crew, distance = 0):
        super().__init__(name, speed, crew)
        self.distance = distance

    def move(self, new_distance):
        self.distance = self.distance + new_distance

    def __str__(self):
        return  f'{self.crew} members of the ship {self.name} overcome {self.distance} of the way on speed {self.speed}.'


s1 = Ship('Victoria', 50, 40)
s1.move(260)
print(s1)

s2 = Ship('Qeen', 30, 25)
s2.move(40)
print(s2)

class Boat(Vessel):

    def __init__(self, name, speed, crew, number_of_sails, distance = 0):
        super().__init__(name, speed, crew)
        self.number_of_sails = number_of_sails
        self.distance = distance

    def move(self, new_distance):
        self.distance = self.distance + new_distance

    def __str__(self):
        return  f'{self.crew} members of the boat {self.name} with {self.number_of_sails} sails overcome {self.distance} of the way on speed {self.speed}.'

b1 = Boat('Princess', 40, 3, 1)
b1.move(60)
print(b1)

class Steamboat(Vessel):

    def __init__(self, name, speed, crew, number_of_engines, distance = 0):
        super().__init__(name, speed, crew)
        self.number_of_engines = number_of_engines
        self.distance = distance

    def move(self, new_distance):
        self.distance = self.distance + new_distance

    def __str__(self):
        return  f'{self.crew} members of the steamboat {self.name} with {self.number_of_engines} engines overcome {self.distance} of the way on speed {self.speed}.'

st1 = Steamboat('Diana', 20, 32, 4)
st1.move(138)
print(st1)