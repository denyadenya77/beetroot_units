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




# Создать класс Ученик наследуя от Person. Создать экземпляры этого класса и добавить в ClassRoom. Переопределить метод displayInfo

class Student(Person):

    def displayInfo(self):
        return f'Student {self.f_name} {self.l_name} is present!'




class School:
  
  subj_teacher = {}

  # Добавить в класс School classmethod для вывода списка преподавателей по конкретному предмету.
  @classmethod
  def subj_teachers_print(cls):
      for k, v in School.subj_teacher.items():
          x = ', '.join(v)
          return f'Subject: {k}, teachers: {x}'




class ClassRoom(School):

    def __init__(self, name, *students):
        self.classrom_name = name
        self.students_names = students

    def displayInfo(self):
        sn = ', '.join([str(x) for x in self.students_names])
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


# Создать класс Учитель наследуя от Person. Переопределить метод displayInfo. Создать экземпляры этого класса и
# добавить в Школу еще одну переменную класса - словарь, где ключ это название предмета а значение - список учителей,
# работающих в данной школе.


class Teacher(Person):

    def __init__(self, f_name, l_name, b_date, subj):
        super().__init__(f_name, l_name, b_date)
        self.subj = subj
        if self.subj not in School.subj_teacher.keys():
            School.subj_teacher[self.subj] = [self.full_name]
        else:
            School.subj_teacher[self.subj].append(self.full_name)



    def displayInfo(self):
        return f'teachers name: {self.full_name}. Subj = {self.subj}'



# Создать класс Урок, с информацией о теме урока, учителе, который ведет урок.

class Lesson:

  def __init__(self, topic, teacher):
    self.topic = topic
    self.teacher = teacher



# Создать класс Расписание. С информацией об уроке, дате урока и классе в котором проходит урок. Добавить метод класса
# set_absent(student_name) - ученик отсутствует на уроке.


class Timetable:

  def __init__(self, date, classroom, lesson_info):
    self.day = date
    self.classroom = classroom
    self.lesson_info = lesson_info
    self.absent = []

  def set_absent(self, *student):
    for x in student:
      self.absent.append(x.full_name)



# ----------------------------------------------------------------------------
print('Создать класс Person с атрибутами имя, фамилия, дата рождения. Добавить методы get_age, displayInfo.')
denys = Person('Denys', 'Kuznetsov', '1997-03-13')
print(denys.age)
print(denys.displayInfo())

print()
print('Добавить в класс Person статический метод для определения является ли человек подростком')
print(denys.is_teen())

print()
print('Создать класс Ученик наследуя от Person. Создать экземпляры этого класса и добавить в ClassRoom. Переопределить метод displayInfo')
alex = Student('Alex', 'Shavlak', '1990-10-10')
vasya = Student('Vasya', 'Vaskin', '1889-10-10')
petya = Student('Petya', 'Pupkin', '1245-13-11')
print(alex.displayInfo())


school_1 = School()


classmates = ClassRoom('404', alex.l_name, vasya.l_name)
classmates_2 = ClassRoom('302', petya)
print(classmates.displayInfo())

print()
print('Создать класс Учитель наследуя от Person. Переопределить метод displayInfo. Создать экземпляры этого класса и'
      ' добавить в Школу еще одну переменную класса - словарь, где ключ это название предмета а значение - список учителей,'
      ' работающих в данной школе.')
daria = Teacher('Daria', 'Tereta', '2000-10-10', 'python')
victor = Teacher('Vit`ok', 'Victorovsky', '4554-12-01', 'python')
oleg = Teacher('Oleg', 'Olegov', '1985-15-15', 'java')
print(daria.displayInfo())
print(school_1.subj_teacher)

print()
print('Создать класс Урок, с информацией о теме урока, учителе, который ведет урок.')
lesson_1 = Lesson('classes', daria)
lesson_2 = Lesson('java', oleg)
print(lesson_1.teacher.full_name)
print(lesson_1.topic)

print()
print('Создать класс Расписание. С информацией об уроке, дате урока и классе в котором проходит урок. Добавить метод класса '
      'set_absent(student_name) - ученик отсутствует на уроке.')
monday = Timetable('25-10-2019', 203, lesson_1)
tuesday = Timetable('30-10-2019', 101, lesson_2)
monday.set_absent(alex, vasya)
print()
print(monday.lesson_info.teacher.full_name)
print(monday.absent)


print()
print('Перегрузить методы __lt__, __gt__, __eq__ для Классов, таким образом чтоб при сравнении двух классов вычислялась разница по количеству учеников.')
print(classmates < classmates_2)

print()
print('Добавить в класс School classmethod для вывода списка преподавателей по конкретному предмету.')
print(school_1.subj_teachers_print())

