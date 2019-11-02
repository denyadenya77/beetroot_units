# Написать класс Wallet с приватными атрибутами класса: dollars, cents. Написать setter, deleter, getter для cents
# и вычисляемый атрибут для общего количества денег.

class Wallet:

    def __init__(self, dollars, cents):
        self._dollars = dollars
        self._cents = cents

    @property
    def total(self):
        return self._dollars + (self._cents / 100)

    @total.setter
    def total(self, total):
        dollars = total[0]
        cents = total[1]
        self._dollars = dollars
        self._cents = cents

    @total.deleter
    def total(self):
        del self._dollars, self._cents
        print('Deleted.')


my_wallet = Wallet(35, 190)
print(my_wallet.total)

my_wallet.total = 40, 150
print(my_wallet.total)

del my_wallet.total
