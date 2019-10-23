import json

def the_right_answer(test, i):
    """ поиск правильного ответа """
    for index, key in enumerate(test):
        if index == i and i != 3:
            right_answer = max(test[key].values())
            for k, v in test[key].items():
                if v == right_answer:
                    return k, v

def the_user_answer(answer, test, i):
    """ поиск ответа пользователя в списке """
    for index, key in enumerate(test):
        if index == i and i != 3:
            for k, v in test[key].items():
                if answer in k:
                    return k, v

def missed_answers(user_test, j):
    """ выводит список из неправильного и правильного ответа """
    for index, key in enumerate(user_test):
        result_list = []
        if index == j and j != 3:
            for k, v in user_test[key].items():
                result_list.append(k)
                result_list.append(v)
            return result_list



test_json = {
    'Выберите ключевые особенности переменной Python': {'1. переменную нужно объявить перед использованием: int var1;': 3,
                                                        '2. Значение переменной нельзя поменять в дальнейшем': 0,
                                                        '3. Значение переменной можно поменять в любой момент': 0},
    'Имена переменной ...': {'1. могут быть разной длинны': 0,
                             '2. могут содержать только буквы': 0,
                             '3. могут содержать буквы любого регистра, цифры и "_"': 3},
    'Что такое PEP?': {'1. руководство по написанию кода Python': 0,
                       '2. документ описывает соглашение о том, как писать код для языка python, а так же содержит предложения по развитию языка': 3,
                       '3. справочник по функциям': 0}, 'total': 9}

with open('test.json', 'w') as file_obj:
    json.dump(test_json, file_obj)

with open('test.json') as file_obj:
    test = json.load(file_obj)

user_test = {}


# вывод вопроса и вариантов ответа.
i = 0

results = [None, None, None]
total_v = 0

# for index, key in enumerate(test):
for key in test.keys():
    # if index == i and i != 3:
    if key == 'total':
        break

    print('')
    print(key)
    for k, v in test[key].items():
        print(k)
    answer = input('Выберите один вариант ответа: ') + '.'

    right_answer = the_right_answer(test, i)
    right_answer_key = right_answer[0]
    right_answer_value = right_answer[1]

    full_user_answer = the_user_answer(answer, test, i)
    full_user_answer_key = full_user_answer[0]
    full_user_answer_value = full_user_answer[1]

    if full_user_answer_key == right_answer_key:
        user_test[key] = {right_answer_key: right_answer_value}
        total_v = total_v + 3
        results[i] = True
    if full_user_answer_key != right_answer_key:
        user_test[key] = {full_user_answer_key: full_user_answer_value, right_answer_key: right_answer_value}
        results[i] = False

    i += 1


# вывод ответов пользователя в консоль.
print('\nВаши ответы: \n')

j = 0

for index, user_test_key in enumerate(user_test):
    if index == j:
        print(f'Вопрос: {user_test_key}')
        if len(user_test[user_test_key]) < 2:
            for k, v in user_test[user_test_key].items():
                print(f'Ваш ответ: {k}\n'
                      f'Выш балл: {v}\n')

        if len(user_test[user_test_key]) == 2:
            wrong_answers = missed_answers(user_test, j)
            print(f'Ваш ответ: {wrong_answers[0]}\n'
                  f'Ваш балл: {wrong_answers[1]}\n'
                  f'Правильный ответ: {wrong_answers[2]}. \n')
    j += 1

print(f'Вы набрали {total_v} баллов.')


with open('test_results.json', 'a') as file_obj:
    json.dump(user_test, file_obj)

# результирующий файл со статистикой.

with open('stat_test.json', 'r') as file_obj:
    stat = json.load(file_obj)


with open('stat_test.json', 'w') as file_obj:
    if results[0]:
        stat['q1'][0] += 1
    elif not results[0]:
        stat['q1'][1] += 1
    if results[1]:
        stat['q2'][0] += 1
    elif not results[1]:
        stat['q2'][1] += 1
    if results[2]:
        stat['q3'][0] += 1
    elif not results[2]:
        stat['q3'][1] += 1
    json.dump(stat, file_obj)

# читаем статистику прохождений.
with open('stat_test.json') as file_obj:
    read = json.load(file_obj)

print(f'\nСтатистика ответов: {read}')