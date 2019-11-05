# Создать класс Карта с свойствами масть и значение. Создать класс Колода, которая будет итератором
# для экземпляров класса Карт.


class Card:

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit


class Deck:

    _deck_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'lady', 'king', 'ace']

    def __init__(self, my_card):
        self.card = my_card
        self.index = (Deck._deck_values.index(self.card.value) - 1)


    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index < len(Deck._deck_values):
            return f'{Deck._deck_values[self.index]} {self.card.suit}'
        else:
            raise StopIteration



a = Card(3, 'dimonds')
b = Deck(a)

print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))