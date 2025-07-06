from datetime import datetime

from database.db_pool import db


class Borrow(db.Model):
    __tablename__ = 'borrow'

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    user_id = db.Column(db.BigInteger, nullable=False,comment='用户id')
    book_id = db.Column(db.BigInteger, nullable=False,comment='图书id')
    created_at = db.Column(db.DateTime, default=datetime.utcnow, comment='创建时间')
    is_return = db.Column(db.Boolean, default=False, comment='是否还书')

    def __init__(self, user_id: int, book_id: int,create_at: datetime, is_return: bool):
        self.user_id = user_id
        self.book_id = book_id
        self.created_at = create_at
        self.is_return = is_return

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'book_id': self.book_id,
            'created_at': self.created_at,
            'is_return': self.is_return
        }

    def __repr__(self):
        return f'<user {self.user_id} Borrow book {self.book_id} at {self.created_at}>'