"""
模型注册文件
确保所有模型都被导入，这样SQLAlchemy才能创建对应的表
"""

# 导入所有模型
from models.book.book import Book
from models.user.user import User

# 导出所有模型
__all__ = ['Book', 'User'] 