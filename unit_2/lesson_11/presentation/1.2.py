# # Создать классы с методами __str__, __repr__ и собственными методами классов, построить правильную иерархию классов.
# # Перечень классов: Автомобиль, Поезд, Транспортное средство, Мотоцикл.

class Vehicle:

    def __init__(self, wheels, passengers):
        self.wheels = wheels
        self.passengers = passengers

    def __str__(self):
        return f'Vehicle got {self.wheels} wheels and can contain {self.passengers} passengers.'

    def __repr__(self):
        return [self.wheels, self.passengers]

class Car(Vehicle):

    def __init__(self, wheels, passengers, brand):
        self.brand = brand
        super().__init__(wheels, passengers)



    def __str__(self):
        return f'Car of brand {self.brand} got {self.wheels} wheels and can contain {self.passengers} passengers.'

    def __repr__(self):
        return [self.wheels, self.passengers, self.brand]

car_1 = Car(4, 5, 'volvo')
print(car_1)
print(car_1.__repr__())


class Motorcycle(Vehicle):

    def __init__(self, wheels, passengers, speed):
        self.speed = speed
        super().__init__(wheels, passengers)

    def __str__(self):
        return f'Motorcycle got {self.wheels} wheels and can contain {self.passengers} passengers. ' \
               f'Max speed = {self.speed}'

    def __repr__(self):
        return [self.wheels, self.passengers, self.speed]

moto_1 = Motorcycle(2, 2, 260)
print(moto_1)
print(moto_1.__repr__())

class Train(Vehicle):

    def __init__(self, wheels, passengers, arriving):
        super().__init__(wheels, passengers)
        self.arriving = arriving

    def __str__(self):
        return f'Train has got {self.wheels} wheels and can contain {self.passengers} passengers. ' \
               f'Arriving at = {self.arriving}'

    def __repr__(self):
        return [self.wheels, self.passengers, self.arriving]

train_1 = Train(72, 600, '2020-13-03 18:40')
print(train_1)
print(train_1.__repr__())