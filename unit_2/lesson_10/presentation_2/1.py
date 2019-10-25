# Создать класс Person с атрибутами имя, фамилия, дата рождения. Добавить методы get_age, displayInfo.

from datetime import date


class Person:

    def __init__(self, f_name, l_name, b_date):
        self.f_name = f_name
        self.l_name = l_name
        self.b_date = b_date
        self.age = Person.get_age(b_date)
        self.full_name = Person.find_full_name(f_name, l_name)

    @classmethod
    def get_age(cls, b_date):
        b_year = int(b_date[0:4])
        t_year = date.today().year
        age = t_year - b_year
        return age

    @classmethod
    def find_full_name(cls, f_name, l_name):
        fn = [f_name, l_name]
        return ' '.join(fn)

    def displayInfo(self):
        person_info = f'Hello, {self.f_name} {self.l_name}! You are {self.age} years old!'
        return person_info


# Создать класс Ученик наследуя от Person. Создать экземпляры этого класса и добавить в ClassRoom.
# Переопределить метод displayInfo

class Student(Person):

    def displayInfo(self):
        return f'Student {self.f_name} {self.l_name} is present!'


class School:
    subj_teacher = {}


class ClassRoom(School):

    def __init__(self, name, *students):
        self.classrom_name = name
        self.students_names = students

    def displayInfo(self):
        sn = ', '.join([str(x) for x in self.students_names])
        person_info = f'Classrom {self.classrom_name}: {sn}.'
        return person_info


# Создать класс Учитель наследуя от Person. Переопределить метод displayInfo. Создать экземпляры этого класса и
# добавить в Школу еще одну переменную класса - словарь, где ключ это название предмета а значение - список учителей,
# работающих в данной школе.


class Teacher(Person):

    def __init__(self, f_name, l_name, b_date, subj):
        super().__init__(f_name, l_name, b_date)
        self.subj = subj
        School.subj_teacher[self.subj] = self.full_name

    def displayInfo(self):
        return f'teachers name: {self.full_name}. Subj = {self.subj}'


# Создать класс Урок, с информацией о теме урока, учителе, который ведет урок.

class Lesson:

    def __init__(self, topic, teacher):
        self.topic = topic
        self.teacher = teacher


# Создать класс Расписание. С информацией об уроке, дате урока и классе в котором проходит урок. Добавить метод класса set_absent(student_name) - ученик отсутствует на уроке.


class Timetable:

    def __init__(self, date, classroom, lesson_info):
        self.date = date
        self.classroom = classroom
        self.lesson_info = lesson_info
        self.absent = []

    def set_absent(self, *student):
        for x in student:
            self.absent.append(x.full_name)


# Вывести информацию про количество уроков в определенный день (вводиться пользователем)

count_of_lessons_day = list(input('Введите дату и кол-во уроков: ').split())
print(f'В день {count_of_lessons_day[0]} {count_of_lessons_day[1]} уроков.')

# ----------------------------------------------------------------------------
danys = Person('Denys', 'Kuznetsov', '1997-03-13')
print(danys.age())

alex = Student('Alex', 'Shavlak', '1990-10-10')
vasya = Student('Vasya', 'Vaskin', '1889-10-10')

school_1 = School()

classmates = ClassRoom('302', alex.l_name, vasya.l_name)
print(classmates.displayInfo())

daria = Teacher('Daria', 'Tereta', '2000-10-10', 'python')
oleg = Teacher('Oleg', 'Olegov', '1985-15-15', 'java')
print()
print(daria.displayInfo())
print(school_1.subj_teacher)

print()
print(lesson_1.teacher.full_name)
print(lesson_2.teacher.full_name)

lesson_1 = Lesson('classes', daria)
lesson_2 = Lesson('java', oleg)

time_t_1 = Timetable('25-10-2019', 203, lesson_1)
time_t_2 = Timetable('25-10-2019', 203, lesson_2)
time_t_1.set_absent(alex, vasya)
print()
print(time_t_1.lesson_info.teacher.full_name)
print(time_t_1.absent)
