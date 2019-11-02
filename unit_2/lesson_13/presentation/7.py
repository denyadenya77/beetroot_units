# Изменить пример make_averager, так чтоб функция хранила результат предыдущей суммы и количество елементов, тогда
# зная эти два числа можно вычислить новое среднее значение. (используйте nonlocal)


def make_averager():
    series = []  # замыкание переменной
    prev_res = 0

    def averager(new_value):  # вложенная функция
        if len(series) == 0:
            series.append(new_value)  # добавить значение в список
            total = sum(series)  # посчитать сумма всех
            nonlocal prev_res
            prev_res = total/len(series)
            return prev_res
        else:
            series.append(new_value)
            prev_res = (prev_res + new_value) / len(series)
            return prev_res
    return averager  # вернуть функцию

avg = make_averager()
print(avg(10))
print(avg(11))
print(avg(12))


# не работает
