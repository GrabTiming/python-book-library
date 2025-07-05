from typing import Dict

from flask import Blueprint, request, current_app

user_bp = Blueprint('user',__name__)


@user_bp.route('',methods=['POST'])
def login() -> Dict[str, str]:
    """
        post请求从表单中获取数据
    """
    username = request.form.get('username',default='')
    password = request.form.get('password',default='')
    current_app.logger.info(f"login user: {username}")
    return {
        'username':username,
        'password':password
    }