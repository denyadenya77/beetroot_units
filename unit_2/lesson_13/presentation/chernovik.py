# Изменить пример make_averager, так чтоб функция хранила результат предыдущей суммы и количество елементов, тогда
# зная эти два числа можно вычислить новое среднее значение. (используйте nonlocal)


def make_averager():
    series = []
    prev_res = 0
    series_len = 0

    def averager(new_value):
        if len(series) == 0:
            series.append(new_value)
            total = sum(series)
            nonlocal prev_res, series_len
            prev_res = total / len(series)
            return prev_res
        elif len(series) > 0:
            series.append(new_value)
            result = (prev_res + new_value) / (series_len + 1)
            series.append(new_value)
            prev_res = result
            series_len = len(series)
            return result

    return averager


avg = make_averager()
print(avg(10))
print(avg(11))
print(avg(12))
