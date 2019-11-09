# Прочесть файл с помощью генератора (генератор будет возвращать по одной прочитанной строке).


def line_reader():
    with open("text.txt", "r") as file:
        line = file.readline()
        while line:
            yield line
            line = file.readline()


a = line_reader()
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
