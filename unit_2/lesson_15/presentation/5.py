# Создать класс Карта с атрибутами значение и масть, перегрузить методы __lt__, __gt__, __eq__ для сравнения карт.

class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value


    def __lt__(self, other):
        if self.suit == other.suit and self.value < other.value:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.suit == other.suit and self.value > other.value:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.suit == other.suit and self.value == other.value:
            return True
        else:
            return False


card_1 = Card('diamonds', 6)
card_2 = Card('diamonds', 9)
card_3 = Card('hearts', 7)

print(card_1 < card_2)
print(card_2 > card_3)
print(card_3 == card_3)