# Создать класс Celcius с приватным атрибутом _temperature. Объявить для этого атрибута setter, getter, deleter.
# Создать вычисляемый атрибут для перевода по фаренгейту.

class Celcius:

    def __init__(self, t):
        self._temperature = t

    @property
    def fahrenheit(self):
        return round(((1.8 * float(self._temperature)) + 32), 1)

    @fahrenheit.setter
    def fahrenheit(self, t_fahrenheit):
        self.celcius = round(((t_fahrenheit - 32) / 1.8), 1)

    @fahrenheit.deleter
    def fahrenheit(self):
        del self.celcius
        print('Deleted.')


t = Celcius(37)
print(t.fahrenheit)

t.fahrenheit = 98.6
print(t.celcius)

del t.fahrenheit
