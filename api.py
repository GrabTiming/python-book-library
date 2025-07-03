"""
程序启动入口
"""
from flask import Flask, request
app = Flask(__name__)
@app.route('/hello')
def hello_world():
    """
    get请求从url中获取数据
    """
    # 这是一个不可变的字典
    params = request.args
    name = params.get('name',default='Lnn')
    return f'Hello, World! {name}'

@app.route('/login',methods=['POST'])
def login():
    """
    post请求从表单中获取数据
    """
    username = request.form.get('username',default='')
    password = request.form.get('password',default='')
    return {
        'username':username,
        'password':password
    }

if __name__ == '__main__':
    app.run(debug=True)