# Создать классы с методами __str__, __repr__ и собственными методами классов, построить правильную иерархию классов.
# Перечень классов: Деталь, Механизм, Изделие.

class Detail:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'Detail name - {self.name}, price - {self.price}'

    def __repr__(self):
        return [self.name, self.price]

forcer = Detail('forcer', 30)
valve = Detail('valve', 10)

class Mechanism(Detail):

    def __init__(self, name, price, *details):
        super().__init__(name, price)
        self.details = details

    def __str__(self):
        l = []
        for x in self.details:
            x_name = x.name
            x_price = x.price
            l_l = [x_name, str(x_price)]
            l_l_l = ' - '.join(l_l)
            l.append(l_l_l)
        str_of_details = ', '.join(l)
        return f'Mechanism {self.name} cost {self.price}, and consists of: {str_of_details}'

    def __repr__(self):
        l = []
        for x in self.details:
            x_name = x.name
            l.append(x_name)
        str_of_details = ', '.join(l)
        return [self.name, self.price, str_of_details]

engine = Mechanism('engine', 3000, forcer, valve)
print(engine)
print(engine.__repr__())

class Product(Detail):

    def __init__(self, name, price, *mechanisms):
        super().__init__(name, price)
        self.mechanisms = mechanisms


    def __str__(self):
        l = []
        for x in self.mechanisms:
            x_name = x.name
            x_price = x.price
            l_l = [x_name, str(x_price)]
            l_l_l = ' - '.join(l_l)
            l.append(l_l_l)
        str_of_mechanisms = ', '.join(l)
        return f'Product {self.name} cost {self.price}, and consists of mechanisms: {str_of_mechanisms}'

    def __repr__(self):
        l = []
        for x in self.mechanisms:
            x_name = x.name
            l.append(x_name)
        str_of_mechanisms = ', '.join(l)
        return [self.name, self.price, str_of_mechanisms]

car = Product('car', 80000, engine)
print(car)
print(car.__repr__())