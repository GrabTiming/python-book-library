"""
程序启动入口
"""

from flask import Flask

from database import db_pool
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

    # 初始化数据库
    db_pool.init_db(app)
    
    # 导入所有模型以确保表被创建
    import models

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='localhost', port=10010)
