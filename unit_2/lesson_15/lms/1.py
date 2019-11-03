# Create a class Person that has at least attributes first_name and
# last_name, use property decorators to create getters and setters for the email
# and fullname, email should be first_name.last_name@email.com
# and fullname just first_name together with last_name separated by a space
# character.


class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def email(self):
        return f'{self.first_name.lower()}.{self.last_name.lower()}@email.com'

    @fullname.setter
    def fullname(self, fullname):
        first_name, last_name = fullname.split()
        self.first_name = first_name
        self.last_name = last_name

    @fullname.deleter
    def fullname(self):
        del self.first_name
        del self.last_name


denys = Person('Denys', 'Kuznetov')
print(denys.fullname)
print(denys.email)

denys.fullname = 'Vasya Pupkin'
print(denys.first_name)
print(denys.last_name)

del denys.fullname