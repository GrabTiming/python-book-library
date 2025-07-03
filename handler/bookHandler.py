from flask import app


class BookHandler:
    # 将 books 作为类变量定义
    book = {
        'title': 'Python',
        'author': 'James',
        'price': 10.0,
        'image': '123',
        'file': '123'
    }
    books = [book]
    def __init__(self):
        pass

    @app.route('/books', methods=['GET'])
    def get_books(self):
        return self.books

    @app.route('/book/add', methods=['POST'])
    def add_book(self, book):
        self.books.append(book)