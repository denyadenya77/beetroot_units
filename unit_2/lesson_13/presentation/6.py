# Написать функцию create_counter, в которой будет объявлена переменная counter и функция generate_password, вернуть
# функцию generate_password. Функция generate_password должна генерировать пароль и увеличивать counter на 1. Вызвать
# функцию для генерации пароля несколько раз и посмотреть как изменится счетчик.

import random


def create_counter():
    counter = 0

    def generate_password():
        gen = [str(x) for x in random.sample(range(100), 10)]
        password = ''.join(gen)
        nonlocal counter
        counter += 1
        print(f'counter: {counter}')
        return password

    return generate_password


a = create_counter()
b = a()
print(b)

c = a()
print(c)

d = a()
print(d)
