# Написать тесты на задания с Unit 2 Lesson 1 Part 2

from unit_2.lesson_10.presentation_2.person_class import Person, Student, Teacher
import unittest


class TestPerson(unittest.TestCase):

    def setUp(self):
        self.denys = Person('Denys', 'Kuznetsov', '1997-03-13')

    def test_get_age(self):
        self.denys.get_age('1997-03-13')
        self.assertEqual(self.denys.age, 22)

    def test_find_full_name(self):
        self.assertEqual(self.denys.find_full_name('Denys', 'Kuznetsov'), 'Denys Kuznetsov')

    def test_displayInfo(self):
        self.assertEqual(self.denys.displayInfo(), 'Hello, Denys Kuznetsov! You are 22 years old!')

    def test_is_teen(self):
        self.assertEqual(self.denys.is_teen(), "Person is not teen")


class TestStudent(unittest.TestCase):

    def setUp(self):
        self.alex = Student('Alex', 'Vasilenko', '1990-05-18')

    def test_get_age(self):
        self.alex.get_age('1990-05-18')
        self.assertEqual(self.alex.age, 29)

    def test_find_full_name(self):
        self.assertEqual(self.alex.find_full_name('Alex', 'Vasilenko'), 'Alex Vasilenko')

    def test_displayInfo(self):
        self.assertEqual(self.alex.displayInfo(), 'Student Alex Vasilenko is present!')


class TestTeacher(unittest.TestCase):

    def setUp(self):
        self.daria = Teacher('Daria', 'Tereta', '2000-10-10', 'python')

    # def test_get_age(self):
    #     self.daria.get_age('2000-10-10')
    #     self.assertEqual(self.daria.age, 29)



if __name__ == '__main__':
    unittest.main()