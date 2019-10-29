# Make a class structure in python representing people in a school. Make a base class called Person,
# a class called Student, and another one called Teacher. Try to find as many methods and attributes
# as you can which belong to the different classes, and keep in mind which are common and which are not.
# For example name should be a Person attribute,while salary should only be available to Teacher.

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} is {self.age} years old.'


class Student(Person):

    def __init__(self, name, age, year_of_study, average_mark, subject):
        super().__init__(name, age)
        self.year_of_study = year_of_study
        self.average_mark = average_mark
        self.subject = subject

    def __str__(self):
        return f'Student {self.name} is {self.age} years old. Subject - {self.subject}. ' \
               f'Average mark - {self.average_mark}'


class Teacher(Person):

    def __init__(self, name, age, subject, salary):
        super(). __init__(name, age)
        self.subject = subject
        self.salary = salary

    def __str__(self):
        return f'Teacher {self.name} is {self.age} years old. Subject - {self.subject}. ' \
               f'Salary mark - {self.salary}'
