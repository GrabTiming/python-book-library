"""
程序启动入口
"""
import json
from sys import prefix
from typing import Dict, List, Any, Optional

from flask import Flask

from routes.book_routes import book_bp


def create_app():
    app = Flask(__name__)

    # 设置全局日志级别（DEBUG/INFO/WARNING/ERROR/CRITICAL）
    app.logger.setLevel("INFO")

    # 注册蓝图
    from routes.common_routes import common_bp
    from routes.user_routes import user_bp
    app.register_blueprint(common_bp,url_prefix='/')
    app.register_blueprint(user_bp,url_prefix='/user')
    app.register_blueprint(book_bp,url_prefix='/book')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='localhost', port=10010)
