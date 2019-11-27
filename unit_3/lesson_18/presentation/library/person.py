class Person:

    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def __str__(self):
        return f'{self.name} {self.last_name}'