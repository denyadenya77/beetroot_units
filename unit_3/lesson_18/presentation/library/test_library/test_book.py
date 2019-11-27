from unittest import mock, TestCase, main
from book import Book


class TestBook(TestCase):

    def setUp(self):
        self.book = Book('Name', 'Author', 'file_path')



    # def test_count_if_lines(self):
    #     open_mock = mock.MagicMock()
    #     with mock.patch('__builtin__.open', open_mock):
    #         self.book.count_of_lines()
    #         open_mock.assert_called()




    @mock.patch('library.open')
    def test_count_if_lines(self, open_mock):
        open_mock.return_value = 'djflsj'
        self.book.count_of_lines()
        open_mock.assert_called()


if __name__ == '__main__':
    main()