import unittest
from unittest import mock
from unit_2.lesson_17.refactor.library import *


class TestBook(unittest.TestCase):

    def setUp(self):
        self.book = Book('Name', 'Author', 'file_path')

    # def test_count_if_lines(self):
    #     open_mock = mock.MagicMock()
    #     with mock.patch('__builtin__.open', open_mock):
    #         self.book.count_of_lines()
    #         open_mock.assert_called()

    # @mock.patch('__builtin__.open')
    # def test_count_if_lines(self, open_mock):
    #     self.book.count_of_lines()
    #     open_mock.assert_called()