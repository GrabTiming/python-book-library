from database.db_pool import db
from datetime import datetime


class User(db.Model):
    """
    用户模型
    """
    __tablename__ = 'users'
    
    # 主键
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    
    # 用户信息
    username = db.Column(db.String(50), unique=True, nullable=False, comment='用户名')
    password_hash = db.Column(db.String(255), nullable=False, comment='密码')
    email = db.Column(db.String(100), unique=True, comment='邮箱')
    nickname = db.Column(db.String(50), comment='昵称')
    avatar = db.Column(db.String(255), comment='头像路径')
    
    # 状态
    is_active = db.Column(db.Boolean, default=True, comment='是否激活')
    is_admin = db.Column(db.Boolean, default=False, comment='是否管理员')
    
    # 时间戳
    created_at = db.Column(db.DateTime, default=datetime.utcnow, comment='创建时间')
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, comment='更新时间')
    last_login = db.Column(db.DateTime, comment='最后登录时间')
    
    def __init__(self, username: str, email: str, password_hash: str, 
                 nickname: str = None, avatar: str = None):
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.nickname = nickname
        self.avatar = avatar

    def to_dict(self):
        """转换为字典"""
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'nickname': self.nickname,
            'avatar': self.avatar,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'last_login': self.last_login.isoformat() if self.last_login else None
        }
    
    def to_json(self):
        """转换为JSON格式"""
        return self.to_dict()
    
    def __repr__(self):
        return f'<User {self.username}>' 