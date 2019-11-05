# Написать функцию-декоратор которая проверяет что функция возвращает валидные JSON данные. Применить декоратор к
# 2м функциям - одна возвращает валидные JSON данные, вторая - нет.

# Unit 2 Lesson 5 presentation
import json


def check(f):
    def wrapper():
        a = f()
        for v in a.values():
            if isinstance(v, str):
                print(a)
            else:
                return '-----'
    return wrapper


@check
def generate_json():
    return {'a': 'b', 'c': 'd'}


@check
def generate_invalid_json():
    return {'a': 1, 'b': 2}


generate_json()
generate_invalid_json()
