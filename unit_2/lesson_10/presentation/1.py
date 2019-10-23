# Создать класс Фигура. Наследовать от него классы Треугольник, Прямоугольник, Квадрат.
# У каждого класса создать метод для подсчета периметра и площади.

class Figure():

    def __init__(self, l):
        self.length = l

    def calc_perimiter(self):
        pass

    def calc_square(self):
        pass

class Triangle(Figure):

    def __init__(self, a, b, c, h):
        self.first_side = a
        self.second_side = b
        self.third_side = c
        self.hight = h

    def calc_perimiter(self):
        return self.first_side + self.second_side + self.third_side

    def calc_square(self):
        return self.third_side * self.hight / 2

class Rectangle(Figure):

    def __init__(self, a, b):
        self.first_side = a
        self.second_side = b

    def calc_perimiter(self):
        return (self.first_side + self.second_side) * 2

    def calc_square(self):
        return  self.first_side * self.second_side

class Square(Figure):

    def calc_perimiter(self):
        return 4 * self.length

    def calc_square(self):
        return self.length * self.length

triangle = Triangle(2, 2, 3, 2)
print(triangle.calc_perimiter())

