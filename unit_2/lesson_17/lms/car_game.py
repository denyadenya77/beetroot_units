# Suppose you are creating a 2D game and you want to have a Car that the player can control: Create a class called Car
# and let it have a speed, direction, and position, implement methods to move left, right, up and down, and change
# speed.Then create a TestCase and write unittest for the methods. Tip: Use the setUp method in the TestCase class.rst


class Car:

    def __init__(self, speed):
        self.speed = speed
        self.direction = None
        self.position = [0, 0]

    def move_left(self):
        self.direction = 'left'
        self.position[0] = self.position[0] - self.speed

    def move_right(self):
        self.direction = 'right'
        self.position[0] = self.position[0] + self.speed

    def move_up(self):
        self.direction = 'up'
        self.position[1]= self.position[1] + self. speed

    def move_down(self):
        self.direction = 'down'
        self.position[1] = self.position[1] - self.speed

    def change_speed(self, new_speed):
        self.speed = new_speed

    def __str__(self):
        return f'{self.speed}, {self.direction}, {self.position}'

car_1 = Car(20)
print(car_1)
car_1.move_left()
print(car_1)
car_1.move_right()
print(car_1)
car_1.move_up()
print(car_1)
car_1.move_down()
print(car_1)
car_1.change_speed(30)
print(car_1)