# Создать классы с методами __str__, __repr__ и собственными методами классов, построить правильную иерархию классов.
# Перечень классов: Журнал, Книга, Печатное издание, Учебник

class Print_edition:

    def __init__(self, pages, cover):
        self.pages = pages
        self.cover = cover

    def __str__(self):
        return f'Print edition has {self.pages} and {self.cover} cover'

    def __repr__(self):
        return [self.pages, self.cover]


class Journal(Print_edition):

    def __init__(self, name, price, pages, cover):
        self.name = name
        self.price = price
        super().__init__(pages, cover)

    def __str__(self):
        return f'Journal {self.name} has {self.pages}, {self.cover} cover and cost {self.price}'

    def __repr__(self):
        return [self.name, self.price, self.pages, self.cover]


class Book(Print_edition):

    def __init__(self, name, author, price, pages, cover):
        self.name = name
        self.author = author
        self.price = price
        super().__init__(pages, cover)

    def __str__(self):
        return f'Book {self.name} of {self.author} has {self.pages}, {self.cover} cover and cost {self.price}'

    def __repr__(self):
        return [self.name, self.author, self.price, self.pages, self.cover]


class Schoolbook(Print_edition):

    def __init__(self, name, subject, price, pages, cover):
        self.name = name
        self.subject = subject
        self.price = price
        super().__init__(pages, cover)

    def __str__(self):
        return f'Schoolbook {self.name} of {self.subject} has {self.pages}, {self.cover} cover and cost {self.price}'

    def __repr__(self):
        return [self.name, self.subject, self.price, self.pages, self.cover]