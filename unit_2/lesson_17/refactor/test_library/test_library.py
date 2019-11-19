import unittest
from unittest.mock import patch
from datetime import datetime, timedelta
from uuid import uuid4
from unit_2.lesson_17.refactor.library import *


class TestPerson(unittest.TestCase):

    def test_init(self):
        denys = Person("Denys", "Kuznetsov")
        self.assertEqual(denys.name, 'Denys')
        self.assertEqual(denys.last_name, "Kuznetsov")

    def test_str(self):
        denys = Person("Denys", "Kuznetsov")
        self.assertEqual(str(denys), "Denys Kuznetsov")


class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.library = Library()
        self.person = Person("Denys", "Kuznetsov")
        self.author = Person('Alber', "Kamu")
        self.book = Book("Book name", self.author, '/path')

    @patch('unit_2.lesson_17.refactor.library.Library.is_person_registered')
    def test_get_book(self, mock_ipr):
        mock_ipr.return_value = False
        self.library.get_book(self.person, self.book)
        mock_ipr.assert_called()


if __name__ == "__main__":
    unittest.main()