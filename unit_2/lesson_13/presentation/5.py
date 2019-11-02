# Создать функцию create_adder, внутри которой будет объявлена функция add_elems(list_of_elems) и будет возвращаться
# эта функция. Вызвать функцию create_adder и сложить несколько рандомных чисел (произвольное количество) с помощью
# add_elems.

import random


def create_adder():
    def add_elems():
        list_of_elems = random.sample(range(100), 10)
        return sum(list_of_elems)
    return add_elems


a = create_adder()
print(a())
