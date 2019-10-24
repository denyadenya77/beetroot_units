test = {
    'Выберите ключевые особенности переменной Python': {'1. переменную нужно объявить перед использованием: int var1;': True,
                                                        '2. Значение переменной нельзя поменять в дальнейшем': False,
                                                        '3. Значение переменной можно поменять в любой момент': False},
    'Имена переменной ...': {'1. могут быть разной длинны': False,
                             '2. могут содержать только буквы': False,
                             '3. могут содержать буквы любого регистра, цифры и "_"': True},
    'Что такое PEP?': {'1. руководство по написанию кода Python': False,
                       '2. документ описывает соглашение о том, как писать код для языка python, а так же содержит предложения по развитию языка': True,
                       '3. справочник по функциям': False}}


class Question:
    i = 0

    def __init__(self, vopros = None, right_ansver = None):
        self.vopros = vopros
        self.right_ansver = right_ansver

    @classmethod
    def question_from_dict(cls, test):
        for index, key in enumerate(test):
            if index == Question.i:
                vopros = key

        Question.i += 1
        return cls(vopros)

    @classmethod
    def finding_right_answer(cls, test):
        for index, key in enumerate(test):
            if index == Question.i:
                for k, v in test.items():
                    if v == True:
                        right_ansver = k
                        return right_ansver




class Answer:
    i = 0

    def __init__(self, otvet_1, otvet_2, otvet_3):
        self.otvet_1 = otvet_1
        self.otvet_2 = otvet_2
        self.otvet_3 = otvet_3



    @classmethod
    def answer_from_dict(cls, test):
        for index, key in enumerate(test):
            if index == Answer.i:
                otvety = [(k, v) for k, v in test[key].items()]
                otvet_1 = otvety[0][0]
                otvet_2 = otvety[1][0]
                otvet_3 = otvety[2][0]

        Answer.i += 1
        return cls(otvet_1, otvet_2, otvet_3)


q1 = Question.question_from_dict(test)
qra1 = Question.finding_right_answer(test)
qa1 = Answer.answer_from_dict(test)
q2 = Question.question_from_dict(test)
qa2 = Answer.answer_from_dict(test)
q3 = Question.question_from_dict(test)
qa3 = Answer.answer_from_dict(test)

print(q1.vopros)
print(qa1.otvet_1)
print(qa1.otvet_2)
print(qa1.otvet_3)
print(f'r a ------------ {qra1.right_ansver}')

print()

print(q2.vopros)
print(qa2.otvet_1)
print(qa2.otvet_2)
print(qa2.otvet_3)

print()

print(q3.vopros)
print(qa3.otvet_1)
print(qa3.otvet_2)
print(qa3.otvet_3)
#

