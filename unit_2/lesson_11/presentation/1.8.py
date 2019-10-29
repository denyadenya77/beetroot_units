# # Создать классы с методами __str__, __repr__ и собственными методами классов, построить правильную иерархию классов.
# # Перечень классов: Игрушка, Продукт(Еда), товар, Молочный продукт. (множественное наслед).


class Product:

    def __init__(self, price):
        self.price = price

    def __str__(self):
        return f'The price is {self.price}'


class Food:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'This is a {self.name}'


class Milk_product(Product, Food):

    def __init__(self, price, name, shelf_life):
        super().__init__(price)
        self.name = name
        self.shelf_life = shelf_life

    def __str__(self):
        return f"Price: {self.price}.\n" \
               f"Name: {self.name}.\n" \
               f"Shelf life: {self.shelf_life}."


milk = Milk_product('20.50', 'Milk', '2019-12-31')
print(milk)


class Toy(Product):

    def __init__(self, price, color):
        super().__init__(price)
        self.color = color

    def __str__(self):
        return f'The price of {self.color} toy is {self.price}'