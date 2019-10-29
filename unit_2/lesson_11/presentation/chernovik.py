class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Phone_number:
    def __init__(self, number):
        self.number = number

# множественное наследование
class Person_and_number(Person, Phone_number):
    def __init__(self, name, age, number):
        super().__init__(name, age)
        # Phone_number.__init__(self, number)
        self.number = number
