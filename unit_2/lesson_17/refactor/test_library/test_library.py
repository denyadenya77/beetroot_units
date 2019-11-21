import unittest
from unittest.mock import patch, Mock
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
        self.author = Person('Albert', "Camus")
        self.author_2 = Person('Jean-Paul', 'Sartre')
        self.book = Book("The Fall", self.author, '/path')
        self.book_2 = Book('The Wall', self.author_2, '/path_2')

    # def tearDown(self):
    #     self.library.dispose()
    #     self.person.dispose()
    #     self.author.dispose()
    #     del self.book

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
        self.library.person_cards.append(Mock(person=self.person))
        is_reg = self.library.is_person_registered(self.person)
        self.assertTrue(is_reg)
        self.library.person_cards.clear()

    def test_is_person_registered_false(self):
        is_not_reg = self.library.is_person_registered(self.person)
        self.assertFalse(is_not_reg)

    @patch('unit_2.lesson_17.refactor.library.uuid4')
    def test_register_person(self, mock_uuid):
        mock_uuid.return_value = 123456
        self.library.register_person(self.person)
        self.assertEqual(self.library.person_cards[0].id, 123456)

    def test_get_person_card(self):
        self.library.person_cards.clear()
        self.library.person_cards.append(Mock(person=self.person))
        person_card = self.library.get_person_card(self.person)
        self.assertEqual(person_card.person, self.person)
        self.library.person_cards.clear()

        with self.assertRaises(Exception):
            self.library.get_person_card(self.person)




    @patch('unit_2.lesson_17.refactor.library.Library.get_person_card')
    def test_get_book_back(self, mock_person_card):
        m = Mock(taken_books=[self.book])
        mock_person_card.return_value = m
        self.library.get_book_back(self.person, self.book)
        self.assertEqual(m.taken_books, [])





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

    # def test_all_available_books(self):
    #     # не стоило делать этот ордер словарем
    #
    #     self.library.all_books.clear()
    #     self.assertEqual(self.library.all_books, [])
    #     self.library.add_books(self.book, self.book_2)
    #     self.library.get_book(self.person, self.book)
    #     self.assertEqual(self.library.all_available_books(), ["The Wall"])









if __name__ == "__main__":
    unittest.main()