"""
数据库连接池
"""
from flask_sqlalchemy import SQLAlchemy

# 创建数据库实例，但不绑定到应用
db = SQLAlchemy()

def init_db(app):
    """
    初始化数据库配置
    
    Args:
        app: Flask应用实例
    """
    # 配置 MySQL 连接（格式：mysql+pymysql://用户名:密码@服务器地址/数据库名）
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/simple-library'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭警告
    
    # 将数据库实例绑定到应用
    db.init_app(app)
    
    # 创建所有表
    with app.app_context():
        db.create_all()

