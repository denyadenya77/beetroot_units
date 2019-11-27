from uuid import uuid4


class Book:

    def __init__(self, name, author, file_path):
        self.name = name
        self.author = author
        self.file_path = file_path
        self.id = uuid4()

    # @property
    # def count_of_lines(self):
    #     with open(self.file_path) as book:
    #         lines_in_book = len(book.readlines())
    #     return lines_in_book