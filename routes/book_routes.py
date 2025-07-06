from typing import Dict, Any

from flask import Blueprint, request, current_app

from models.book.book import Book
from database.db_pool import db

book_bp = Blueprint('book', __name__)

@book_bp.route('/add', methods=['POST'])
def add_book() -> Dict[str, Any]:
    """
    添加图书
    """
    try:
        data = request.json
        if not data:
            return {
                'code': 400,
                'message': '请求数据不能为空'
            }
        
        # 创建新图书
        book = Book(
            name=data.get('name','无名图书'),
            author=data.get('author', '未知作者'),
            desc=data.get('desc','暂无简介'),
            price=data.get('price', 0.0),
            cover_pic=data.get('cover_pic','暂无封面'),
            file=data.get('file')
        )
        
        # 保存到数据库
        db.session.add(book)
        db.session.commit()
        
        current_app.logger.info(f"添加图书成功: {book.name}")
        return {
            'code': 200,
            'message': 'success',
            'data': book.to_dict()
        }
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(f"添加图书失败: {str(e)}")
        return {
            'code': 500,
            'message': f'添加图书失败: {str(e)}'
        }

@book_bp.route('/list', methods=['GET'])
def get_books() -> Dict[str, Any]:
    """
    获取所有图书列表
    """
    try:
        params = request.args
        page_num = int(params.get('page_num', 1))
        page_size = int(params.get('page_size', 10))
        book_name = params.get('book_name', '')
        desc = params.get('desc', '')
        
        # 构建查询
        query = Book.query
        
        # 按书名搜索
        if book_name:
            query = query.filter(Book.name.like(f'%{book_name}%'))
        
        # 按描述搜索
        if desc:
            query = query.filter(Book.desc.like(f'%{desc}%'))
        
        # 分页
        pagination = query.paginate(
            page=page_num, 
            per_page=page_size, 
            error_out=False
        )
        
        books = pagination.items
        
        current_app.logger.info(f"查询图书列表: 第{page_num}页，共{len(pagination.total)}本")
        
        return {
            'code': 200,
            'data': [book.to_dict() for book in books],
            'pagination': {
                'page': page_num,
                'per_page': page_size,
                'total': pagination.total,
                'pages': pagination.pages
            }
        }
    except Exception as e:
        current_app.logger.error(f"查询图书列表失败: {str(e)}")
        return {
            'code': 500,
            'message': f'查询图书列表失败: {str(e)}'
        }

@book_bp.route('/<int:book_id>', methods=['GET'])
def get_book(book_id: int) -> Dict[str, Any]:
    """
    根据ID获取指定图书
    """
    try:
        current_app.logger.info(f"查询图书ID: {book_id}")
        
        book = Book.query.get(book_id)
        if not book:
            return {
                'code': 404,
                'message': f'图书ID {book_id} 不存在'
            }
        
        return {
            'code': 200,
            'data': book.to_dict()
        }
    except Exception as e:
        current_app.logger.error(f"查询图书失败: {str(e)}")
        return {
            'code': 500,
            'message': f'查询图书失败: {str(e)}'
        }

@book_bp.route('/<int:book_id>', methods=['PUT'])
def update_book(book_id: int) -> Dict[str, Any]:
    """
    更新图书信息
    """
    try:
        book = Book.query.get(book_id)
        if not book:
            return {
                'code': 404,
                'message': f'图书ID {book_id} 不存在'
            }
        
        data = request.json
        if data.get('name'):
            book.name = data['name']
        if data.get('author'):
            book.author = data['author']
        if data.get('desc'):
            book.desc = data['desc']
        if data.get('price') is not None:
            book.price = data['price']
        if data.get('cover_pic'):
            book.cover_pic = data['cover_pic']
        if data.get('file'):
            book.file = data['file']
        
        db.session.commit()
        
        current_app.logger.info(f"更新图书成功: {book.name}")
        return {
            'code': 200,
            'message': 'success',
            'data': book.to_dict()
        }
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(f"更新图书失败: {str(e)}")
        return {
            'code': 500,
            'message': f'更新图书失败: {str(e)}'
        }

@book_bp.route('/<int:book_id>', methods=['DELETE'])
def delete_book(book_id: int) -> Dict[str, Any]:
    """
    删除图书
    """
    try:
        book = Book.query.get(book_id)
        if not book:
            return {
                'code': 404,
                'message': f'图书ID {book_id} 不存在'
            }
        
        db.session.delete(book)
        db.session.commit()
        
        current_app.logger.info(f"删除图书成功: {book.name}")
        return {
            'code': 200,
            'message': 'success'
        }
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(f"删除图书失败: {str(e)}")
        return {
            'code': 500,
            'message': f'删除图书失败: {str(e)}'
        }