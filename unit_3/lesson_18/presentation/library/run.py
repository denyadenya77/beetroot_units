from library import Library
from person import Person
from book import Book


if __name__ == '__main__':
    den = Person('denis', 'kuzn')
    book = Book("Book name", 'self.author', '/path')
    lib_1 = Library()
    lib_1.add_books(book)
    lib_1.get_book(den, book)
    pc = lib_1.get_person_card(den)
    print(lib_1.book_count)