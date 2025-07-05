import json
from typing import List, Dict, Any

from flask import Blueprint, request, current_app

from entity.book.book import Book

book_bp = Blueprint('book',__name__)

books: List[Book] = []

@book_bp.route('/add',methods=['POST'])
def add_book() -> Dict[str, Any]:
    """
    添加图书
    """
    data = request.json
    book = Book(**data)
    books.append(book)
    current_app.logger.info(f"now the books have {len( books)} books")
    return {
        'code': 200,
        'message': 'success',
        'data': book.to_json()
    }

@book_bp.route('/list',methods=['GET'])
def get_books() -> Dict[str, Any]:

    """
    获取所有图书列表
    """

    params = request.args
    page_num = params.get('page_num', default=1)
    page_size = params.get('page_size', default=10)
    book_name = params.get('book_name', default='')
    desc = params.get('desc', default='')

    result = [book.to_json() for book in books]

    return {
        'code': 200,
        'data': result
    }

@book_bp.route('<id>',methods=['GET'])
def get_book(id) -> Dict[str, Any]:
    """
    根据ID获取指定图书
    """
    current_app.logger.info(f"now you are searching the book {id}")
    if len(books) <=0:
        return {
            'code': 200,
            'message': 'no books'
        }
    id = min(id,len(books)-1)
    return {
        'code': 200,
        'data': books[id]
    }