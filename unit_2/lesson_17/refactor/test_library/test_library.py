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

    # def tearDown(self):
    #     self.library.dispose()
    #     self.person.dispose()
    #     self.author.dispose()
    #     self.book.dispose()

    @patch('unit_2.lesson_17.refactor.library.Library.is_person_registered')
    def test_get_book(self, mock_ipr):
        mock_ipr.return_value = False
        self.library.get_book(self.person, self.book)
        mock_ipr.assert_called()
        self.library.person_cards.clear()  # очищаем self.person_cards для отработки других тестов

    def test_add_books(self):
        self.assertEqual(self.library.all_books, [])
        self.library.add_books(self.book)
        self.assertEqual(self.library.all_books, [self.book])

    def test_is_person_registered(self):
        isperreg_1 = self.library.is_person_registered(self.person)
        self.assertEqual(isperreg_1, False)
        self.library.register_person(self.person)
        isperreg_2 = self.library.is_person_registered(self.person)
        self.assertEqual(isperreg_2, True)
        self.library.person_cards.clear()  # очищаем self.person_cards для отработки других тестов

    def test_register_person(self):
        self.assertEqual(self.library.person_cards, [])
        self.library.register_person(self.person)
        person_card = self.library.get_person_card(self.person)
        self.assertIn(person_card, self.library.person_cards)

    def test_get_person_card(self):
        # написать проверку возврата функции
        self.library.register_person(self.person)
        person_card = self.library.get_person_card(self.person)
        for card in self.library.person_cards:
            if self.person == card.name:
                self.assertEqual(card, person_card)
        self.library.person_cards.clear()  # очищаем self.person_cards для отработки других тестов
        with self.assertRaises(Exception):
            self.library.get_person_card(self.person)

    def test_get_book_back(self):
        self.library.add_books(self.book)
        self.library.get_book(self.person, self.book)
        person_card = self.library.get_person_card(self.person)
        for one_dict in person_card.taken_books:
            for v in one_dict.values():
                if v == self.book:
                    self.assertEqual(v, self.book)
        self.library.person_cards.clear()  # очищаем self.person_cards для отработки других тестов

    def test_book_count(self):
        self.library.all_books.clear()
        self.library.add_books(self.book)
        self.assertEqual(self.library.book_count, 1)








if __name__ == "__main__":
    unittest.main()