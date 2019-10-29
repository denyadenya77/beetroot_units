# Создать классы с методами __str__, __repr__ и собственными методами классов, построить правильную иерархию классов.
# Перечень классов: Тест, Экзамен, Выпускной экзамен, Испытания.


class Trials:

    def __init__(self, questions, max_mark):
        self.questions = questions
        self.max_mark = max_mark


    def __str__(self):
        return f'Trials consist of {self.questions} questions. You can get {self.max_mark} mark.'

    def __repr__(self):
        return [self.questions, self.max_mark]


class Test(Trials):

    def __init__(self, subject, questions, max_mark):
        self.subject = subject
        super().__init__(questions, max_mark)

    def __str__(self):
        return f'Test of {self.subject} consist of {self.questions} questions. You can get {self.max_mark} mark.'

    def __repr__(self):
        return [self.subject, self.questions, self.max_mark]


class Exam(Trials):

    def __init__(self, type, subject, questions, max_mark):
        self.type = type
        self.subject = subject
        super().__init__(questions, max_mark)

    def __str__(self):
        return f'{self.subject} exam consist of {self.questions} {self.type} questions. You can get {self.max_mark} mark.'

    def __repr__(self):
        return [self.type, self.subject, self.questions, self.max_mark]


class Final_exam(Exam):

    def __init__(self, date, type, subject, questions, max_mark):
        self.date = date
        super().__init__(type, subject, questions, max_mark)


    def __str__(self):
        return f'Final exam of {self.subject} consist of {self.questions} {self.type} questions. Date - {self.date}.' \
               f' You can get {self.max_mark} mark.'


    def __repr__(self):
        return [self.date, self.type, self.subject, self.questions, self.max_mark]