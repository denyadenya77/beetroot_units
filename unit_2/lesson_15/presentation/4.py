# Создать класс USDCurrencyConverter, с приватным атрибутом current_value (в USD) и вычисляемыми атрибутами для
# перевода из USD в другие валюты, например EUR, UAH.


class USDCurrencyConverter:

    def __init__(self, USD):
        self._current_value = USD

    @property
    def converted_to_UAH(self):
        return self._current_value * 24.93

    @property
    def converted_to_EUR(self):
        return self._current_value * 0.90


money = USDCurrencyConverter(300)
print(money.converted_to_UAH)

print(money.converted_to_EUR)