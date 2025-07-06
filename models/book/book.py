import decimal

from database.db_pool import db
from datetime import datetime


class Book(db.Model):
    """
    图书模型
    """
    __tablename__ = 'book'
    
    # 主键
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    
    # 图书信息
    name = db.Column(db.String(100), nullable=False, comment='图书名称')
    author = db.Column(db.String(50), nullable=False, comment='作者')
    desc = db.Column(db.Text, comment='图书描述')
    price = db.Column(db.Numeric(10, 2), default=0.00, comment='价格')
    cover_pic = db.Column(db.String(255), comment='封面图片路径')
    file = db.Column(db.String(255), comment='文件路径')
    
    # 时间戳
    created_at = db.Column(db.DateTime, default=datetime.utcnow, comment='创建时间')
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, comment='更新时间')
    
    def __init__(self, name: str, author: str, desc: str = None, price: decimal.Decimal = 0.0,
                 cover_pic: str = None, file: str = None):
        self.name = name
        self.author = author
        self.desc = desc
        self.price = price
        self.cover_pic = cover_pic
        self.file = file

    def to_dict(self):
        """转换为字典"""
        return {
            'id': self.id,
            'name': self.name,
            'author': self.author,
            'desc': self.desc,
            'price': float(self.price) if self.price else 0.0,
            'cover_pic': self.cover_pic,
            'file': self.file,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
    
    def to_json(self):
        """转换为JSON格式"""
        return self.to_dict()
    
    def __repr__(self):
        return f'<Book {self.name} by {self.author}>'