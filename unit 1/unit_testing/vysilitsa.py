# Записать в файл слова, которые нужно будет угадать. В коде открыть файл и выбрать рандомно одно слово,
# которое пользователь должен угадать. Дальше просим пользователя ввести по одной букве в слове.
# Если такой буквы нет - рисуем человечка на виселице.

import random

# поэтапное подвешивание человека.
def losing(mistakes, vysilitsa_list):
    if mistakes == 1:
        vysilitsa_list[1][6] = '!'
    if mistakes == 2:
        vysilitsa_list[2][6] = 'O'
    if mistakes == 3:
        vysilitsa_list[3][6] = '!'
        vysilitsa_list[3][5] = '-'
        vysilitsa_list[3][7] = '-'
    if mistakes == 4:
        vysilitsa_list[4][6] = '!'
        vysilitsa_list[4][4] = '/'
        vysilitsa_list[4][8] = r'\\'[:-1]
    if mistakes == 5:
        vysilitsa_list[5][6] = '!'
    if mistakes == 6:
        vysilitsa_list[6][6] = '-'
        vysilitsa_list[6][5] = '/'
        vysilitsa_list[6][7] = r'\\'[:-1]
    if mistakes == 7:
        vysilitsa_list[7][5] = '!'
        vysilitsa_list[7][7] = '!'
    if mistakes == 8:
        vysilitsa_list[8][5] = '!'
        vysilitsa_list[8][7] = '!'


# читаем файл, выбираем слово, дробим на буквы.
with open('words.txt') as file_obj:
    str_words = file_obj.read()
    list_of_words = str_words.split()
    print(list_of_words)

quiz_word = list(random.choice(list_of_words))
print(quiz_word)

# собираем виселицу.
vysilitsa_list = []
for x in range(11):
    vysilitsa_list.append(list(' ' * 11))

for x in range(11):
    vysilitsa_list[0][x] = '--'
    vysilitsa_list[10][x] = '--'
    vysilitsa_list[x][0] = ';'


# подсчет ошибок и сбор букв.
mistakes = 0
attempts = []

# Отгаданное вами в слове сейчас выглядит так:
word_in_process = list('-' * len(quiz_word))


while mistakes < 8:
    user = input('Введите одну букву: ').lower()
    if user in quiz_word:
        print('Эта буква есть в слове!')

        for sub_list in vysilitsa_list:
            print(' '.join([str(x) for x in sub_list]))

        attempts.append(user)


        i = quiz_word.index(user)
        word_in_process[i] = user


        print('Вы предлагали след. буквы: ')
        print(attempts)

        print('Отгаданное вами в слове сейчас выглядит так:')
        print(' '.join([x for x in word_in_process]))

    elif user not in quiz_word:
        mistakes += 1
        print('Этой буквы нет в слове!')
        losing(mistakes, vysilitsa_list)

        for sub_list in vysilitsa_list:
            print(' '.join([str(x) for x in sub_list]))

        attempts.append(user)

        print('Вы предлагали след. буквы: ')
        print(attempts)

        print('Отгаданное вами в слове сейчас выглядит так:')
        print(' '.join([x for x in word_in_process]))


if mistakes == 8:
    print('Вас повесили!')
    for sub_list in vysilitsa_list:
        print(' '.join([str(x) for x in sub_list]))
elif quiz_word == word_in_process:
    print('Вы победили!')


