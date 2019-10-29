# Создать классы с методами __str__, __repr__ и собственными методами классов, построить правильную иерархию классов.
# Перечень классов: Студент, Преподаватель, Персона, Зав. кафедрой.

class Person:

    def __init__(self, name, age, p_number):
        self.name = name
        self.age = age
        self.p_number = p_number

    def __str__(self):
        return f'\nPerson name: {self.name}. ' \
               f'\nPerson age: {self.age}. ' \
               f'\nPhone number: {self.p_number}'

    def __repr__(self):
        return [self.name, self.age, self.p_number]

denys = Person('Denys Kuznetsov', 22, '0997683348')
print(denys)
print(denys.__repr__())

class Student(Person):

    def __init__(self, name, age, p_number, subject, course):
        self.subject = subject
        self.course = course
        super().__init__(name, age, p_number)

    def __str__(self):
        return f'\nPerson name: {self.name}. ' \
               f'\nPerson age: {self.age}. ' \
               f'\nPhone number: {self.p_number}' \
               f'\nStudent subject: {self.subject}' \
               f'\nStudent course: {self.course}'

    def __repr__(self):
        return [self.name, self.age, self.p_number, self.subject, self.course]


alex = Student('Alex Alex', 25, '0975683399', 'python', 2)
print(alex)
print(alex.__repr__())

class Teacher(Person):

    def __init__(self, name, age, p_number, subject, academic_degree):
        self.subject = subject
        self.academic_degree = academic_degree
        super().__init__(name, age, p_number)

    def __str__(self):
        return f'\nPerson name: {self.name}. ' \
               f'\nPerson age: {self.age}. ' \
               f'\nPhone number: {self.p_number}' \
               f'\nTeacher subject: {self.subject}' \
               f'\nTeacher academic degree: {self.academic_degree}'

    def __repr__(self):
        return [self.name, self.age, self.p_number, self.subject, self.academic_degree]

vasya = Teacher('Vasya Pupkin', 99, '0995692255', 'java', 'otstoy')
daria = Teacher('Daria Tereta', 25, '0662548877', 'python', 'super_krutoy_teacher')
print(daria)
print(daria.__repr__())

class Head_of_department(Person):

    def __init__(self, name, age, p_number, *teachers):
        self.teachers = teachers
        super().__init__(name, age, p_number)

    def __str__(self):
        t = [x.name for x in self.teachers]
        c = ' '.join(t)
        return f'\nPerson name: {self.name}. ' \
               f'\nPerson age: {self.age}. ' \
               f'\nPhone number: {self.p_number}' \
               f'\nTeachesrs of dep.: {c}'

    def __repr__(self):
        t = [x.name for x in self.teachers]
        return [self.name, self.age, self.p_number, t]

ludmila_fedorovna = Head_of_department('Lubanya Lubovkina', 999, 'nikto_ne_znayet', daria, vasya)
print(ludmila_fedorovna)
print(ludmila_fedorovna.__repr__())