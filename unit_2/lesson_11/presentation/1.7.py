# Создать классы с методами __str__, __repr__ и собственными методами классов, построить правильную иерархию классов.
# Перечень классов: Служащий, Персона, Рабочий, Инженер.


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} is {self.age} years old.'

    def __repr__(self):
        return [self.name, self.age]

class Worker(Person):

    def __init__(self, specialty, name, age):
        self.specialty = specialty
        super().__init__(name, age)

    def __str__(self):
        return f'{self.name} is  a specialist in {self.specialty}, and is {self.age} years old.'

    def __repr__(self):
        return [self.name, self.age, self.specialty]


class Employee(Person, Worker):

    def __init__(self, name, age, specialty, salary):
        self.salary = salary
        super().__init__(name, age)
        self.specialty = specialty

    def __str__(self):
        return f'{self.name} is  a specialist in {self.specialty}, and is {self.age} years old. Salary - {self.salary}.'

    def __repr__(self):
        return [self.name, self.age, self.specialty, self.salary]


class Engineer(Person):

    def __init__(self, name, age, qualification):
        super().__init__(name, age)
        self.qualification = qualification

    def __str__(self):
        return f'{self.name} is an engineer, and is {self.age} years old. Qualification - {self.qualification}.'

    def __repr__(self):
        return [self.name, self.age, self.qualification]