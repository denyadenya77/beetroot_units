# Создать класс Person с атрибутами имя, фамилия, дата рождения. Добавить методы get_age, displayInfo.

from datetime import date


class Person:

    def __init__(self, f_name, l_name, b_date):
        self.f_name = f_name
        self.l_name = l_name
        self.b_date = b_date
        self.age = Person.get_age(b_date)


    @classmethod
    def get_age(cls, b_date):
        b_year = int(b_date[0:4])
        t_year = date.today().year
        age = t_year - b_year
        return age

    def displayInfo(self):
        person_info = f'Hello, {self.f_name} {self.l_name}! You are {self.age} years old!'
        return person_info


danys = Person('Denys', 'Kuznetsov', '1997-03-13')
print(danys.displayInfo())


# Создать класс Ученик наследуя от Person. Создать экземпляры этого класса и добавить в ClassRoom.
# Переопределить метод displayInfo

class Student(Person):

    def displayInfo(self):
        return f'Student {self.f_name} {self.l_name} is present!'



alex = Student('Alex', 'Shavlak', '1990-10-10')
vasya = Student('Vasya', 'Vaskin', '1889-10-10')


class ClassRoom:

    def __init__(self, name, *students):
        self.classrom_name = name
        self.students_names = students

    def displayInfo(self):
        sn = ', '.join([str(x) for x in self.students_names])
        person_info = f'Classrom {self.classrom_name}: {sn}.'
        return person_info



classmates = ClassRoom('302', alex.l_name, vasya.l_name)
print(classmates.displayInfo())

# Создать класс Учитель наследуя от Person. Переопределить метод displayInfo. Создать экземпляры этого класса и
# добавить в Школу еще одну переменную класса - словарь, где ключ это название предмета а значение - список учителей,
# работающих в данной школе.


class Teacher(Person):

    def __init__(self, f_name, l_name, b_date, subj):
        super.__init__(f_name, l_name, b_date)
        self.subj = subj


    def displayInfo(self):
        return f'teachers name: {self.f_name} {self.l_name}. '


