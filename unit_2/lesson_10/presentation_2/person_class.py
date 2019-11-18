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

    # Добавить в класс Person статический метод для определения является ли человек подростком в
    # зависимости от возраста: 16 < age > 13
    def is_teen(self):
        if 16 < self.age > 13:
            return "Person is not teen"
        else:
            return "Person is teen"


# Создать класс Ученик наследуя от Person. Создать экземпляры этого класса и добавить в ClassRoom. Переопределить метод displayInfo.

class Student(Person):

    def __init__(self, f_name, l_name, b_date):
        super().__init__(f_name, l_name, b_date)
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
        return f'Student {self.f_name} {self.l_name} is present!'


# Создать класс Учитель наследуя от Person. Переопределить метод displayInfo. Создать экземпляры этого класса и
# добавить в Школу еще одну переменную класса - словарь, где ключ это название предмета а значение - список учителей,
# работающих в данной школе.


class Teacher(Person):

    def __init__(self, f_name, l_name, b_date, subj):
        super().__init__(f_name, l_name, b_date)
        self.age = Person.get_age(b_date)
        self.full_name = Person.find_full_name(f_name, l_name)
        self.subj = subj

        if self.subj not in School.subj_teacher.keys():
            School.subj_teacher[self.subj] = [self.full_name]
        else:
            School.subj_teacher[self.subj].append(self.full_name)

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
        return f'teachers name: {self.full_name}. Subj = {self.subj}'


class School:
    subj_teacher = {}

    # Добавить в класс School classmethod для вывода списка преподавателей по конкретному предмету.
    @classmethod
    def subj_teachers_print(cls):
        a = []
        for k, v in School.subj_teacher.items():
            x = ', '.join(v)
            z = f'{k} - {x}'
            a.append(z)
        return '. '.join(a)


class ClassRoom(School):

    def __init__(self, name, *students):
        self.classrom_name = name
        self.students_names = students

    def displayInfo(self):
        sn = ', '.join([str(x.full_name) for x in self.students_names])
        person_info = f'Classrom {self.classrom_name}: {sn}.'
        return person_info

    # Перегрузить методы __lt__, __gt__, __eq__ для Классов, таким образом чтоб при сравнении двух классов
    # вычислялась разница по количеству учеников.

    def __lt__(self, other):
        if len(self.students_names) < len(other.students_names):
            return True
        else:
            return False

    def __gt__(self, other):
        if len(self.students_names) > len(other.students_names):
            return True
        else:
            return False

    def __eq__(self, other):
        if len(self.students_names) == len(other.students_names):
            return True
        else:
            return False


# Создать класс Урок, с информацией о теме урока, учителе, который ведет урок.

class Lesson:

    def __init__(self, topic, teacher):
        self.topic = topic
        self.teacher = teacher
        self.absent_students = []


# Создать класс Расписание. С информацией об уроке, дате урока и классе в котором проходит урок.

class Timetable:

    def __init__(self, day, *lessons):
        self.day = day
        self.lessons = lessons

    # Добавить метод класса set_absent(student_name) - ученик отсутствует на уроке.
    def set_absent(self, lesson, *absent_students):
        if lesson in self.lessons:
            for x in absent_students:
                lesson.absent_students.append(x)

    # Вывести кто отсутствовал на конкретном уроке за конкретный день (вводиться пользователем).
    def get_absent(self, lesson):
        if lesson in self.lessons:
            a = []
            for x in lesson.absent_students:
                a.append(x.full_name)
            b = ', '.join(a)
            return f'{lesson.topic} absent students: {b}'

    # Вывести информацию про количество уроков в определенный день (вводиться пользователем).
    def count_lessons(self):
        a = len(self.lessons)
        return f'There are {a} lessons on {self.day}'





denys = Person('Denys', 'Kuznetsov', '1997-03-13')
# print(denys.age)
# print(denys.full_name)
# print(denys.is_teen())


alex = Student('Alex', 'Vasilenko', '1990-05-18')
misha = Student('Misha', 'Malachov', '1995-06-22')
petya = Student('Petya', 'Pet`kyn', '1899-09-30')


school_1 = School
classroom_402 = ClassRoom('402', alex, misha)
classroom_101 = ClassRoom('101', petya)
# print(classroom_402.displayInfo()) # словарь предметов и учителей


daria = Teacher('Daria', 'Tereta', '2000-10-10', 'python')
victor = Teacher('Vit`ok', 'Victorovsky', '4554-12-01', 'python')
oleg = Teacher('Oleg', 'Olegov', '1985-15-15', 'java')
# print(school_1.subj_teachers_print())


lesson_1 = Lesson('python', daria)
lesson_2 = Lesson('java', oleg)


monday = Timetable('monday', lesson_1, lesson_2)
monday.set_absent(lesson_1, denys, alex)
# print(monday.get_absent(lesson_1))
# print(monday.count_lessons())


# if classroom_402 > classroom_101:
    # print("classroom_402 > classroom_101")