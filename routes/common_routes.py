from sys import exception

from flask import request, current_app, Blueprint

from database.db_pool import db
from models import User

common_bp = Blueprint('common', __name__)


@common_bp.route('login', methods=['POST'])
def login():
    username = request.json.get('username', default=None)
    password = request.json.get('password', default=None)
    if username and password:
        data = {
            'username': username,
            'password': password
        }
        return {
            'code': 200,
            'data': data
        }
    return {
        'code': 520,
        'message': '缺少参数'
    }

@common_bp.route('register', methods=['POST'])
def register():
    username = request.json.get('username', default=None)
    password = request.json.get('password', default=None)
    if username is None or password is None:
        return {
            'code': 520,
            'message': '缺少参数'
        }

    try:
        user = User(username=username, password_hash=password, email='', nickname=username, avatar='')

        db.session.add(user)
        db.session.commit()

        current_app.logger.info(f"新注册用户: {user.username}")

        return {
            'code': 200,
            'msg': 'ok'
        }
    except exception as e :
        db.session.rollback()
        current_app.logger.error(f"用户注册失败: {str(e)}")
        return {
            'code': 520,
            'msg': '用户注册失败'
        }


@common_bp.route('hello')
def hello():
    """
        get请求从url中获取数据
    """
    # 这是一个不可变的字典
    params = request.args
    name = params.get('name', default='Lnn')
    # 使用current_app来访问应用级别的logger
    current_app.logger.info(f'name: {name}')
    return f'Hello, World! {name}'