# Создать классы с методами __str__, __repr__ и собственными методами классов, построить правильную иерархию классов.
# Перечень классов: Республика, Монархия, Королевство, государство.

class Country:

    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __str__(self):
        return f'Country name - {self.name}, population - {self. population}.'

    def __repr__(self):
        return [self.name, self. population]


class Republic(Country):

    def __init__(self, name, population, head):
        super().__init__(name, population)
        self.head = head

    def __str__(self):
        return f'Country name - {self.name}, population - {self. population}, head - {self.head}.'

    def __repr__(self):
        return [self.name, self. population, self.head]



class Monarchy:

    def __init__(self, head, royal_court):
        self.head = head
        self.royal_court = royal_court

    def __str__(self):
        return f'Monarch name - {self.head}, oyal court consists of {self.royal_court} members.'

    def __repr__(self):
        return [self.head, self.royal_court]


class Kingdom(Country, Monarchy):

    def __init__(self, name, population, head, royal_court):
        super().__init__(name, population)
        self.head = head
        self.royal_court = royal_court

    def __str__(self):
        return f'Country name - {self.name}, population - {self. population}, head - {self.head}, royal court consists ' \
               f'of {self.royal_court} members.'

    def __repr__(self):
        return [self.name, self. population, self.head, self.royal_court]