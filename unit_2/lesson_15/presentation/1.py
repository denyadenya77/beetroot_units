# Написать класс Distance с приватным атрибутом _distance (в метрах). Объявить для этого атрибута setter, getter,
# deleter, который будет показывать дистанцию в метрах. Создать вычисляемый атрибут для перевода дистанции в шаги
# (in_feet, 1м = 0.67 шагов)

class Distance:

    def __init__(self, distance):
        self._distance = distance
        self.steps = self.in_steps()

    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, distance):
        self._distance = distance

    @distance.deleter
    def distance(self):
        del self._distance
        print('Deleted')

    def in_steps(self):
        self.steps = self._distance // 0.67
        return self.steps


d = Distance(2003)
print(d.distance)
print(d.steps)

d.distance = 1000
print(d.distance)

del d.distance