from datetime import datetime


class PersonCard:

    def __init__(self, person, id):
        self.person = person
        self.id = id
        self.date_of_register = datetime.now()
        self.taken_books = []

    def take_book(self, order):
        self.taken_books.append(order)

    def show_all_books_info(self):
        """вывести на экран информацию о пользователе и книгах которые у него на руках"""
        books = [book.name for book in self.taken_books]
        str_books = ', '.join(books)
        return f'User name: {self.person}.\n' \
               f'User ID: {self.id}.\n' \
               f'Date of registration: {self.date_of_register}.\n' \
               f'Taken books: {str_books}.'
