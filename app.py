from flask import Flask,render_template, redirect, url_for, abort
import socket
from datetime import datetime

app = Flask(__name__)

@app.template_filter('born_year')
def calcurate_born_year(age):
    now_timestamp = datetime.now()
    return str(now_timestamp.year - int(age)) + '年'


@app.template_filter('reverse_name')
def reverse(name):
    return name[-1::-1]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index2.html')

@app.route('/hello/<string:name>/<int:age>')
def hello(name, age):
    return render_template('hello.html', name=name, age=age)

class UserInfo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

@app.route('/userlist')
def user_list():
    #users = [
    #    'Taro','jiro','Saburo','Shiro','Hanako','Masa'
    #]
    users = [
        UserInfo('Taro',21),
        UserInfo('Jiro',32),
        UserInfo('Hanako',21)
    ]



    is_login = False
    host = socket.gethostname()
    my_host = "MasahironoMacBook-Pro.local"

    if host == my_host:
        return render_template('userlist.html', host=host,users=users, is_login=is_login)
    else:
        return render_template('index.html', host=host,users=users, is_login=is_login)

@app.route('/user/<string:user_name>/<int:age>')
def user(user_name, age):
    if user_name in ['Taro', 'Jiro', 'Saburo']:
        return redirect(url_for('hello',name=user_name,age=age))
    else:
        abort(500,'そのユーザーはリダイレクトできません')

@app.errorhandler(500)
def system_error(error):
    error_description = error.description
    return render_template('system_error.html', error_description=error_description),500

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':

    host = socket.gethostname()
    my_host = "MasahironoMacBook-Pro.local"

    if host == my_host:
        app.run(debug=True)
    else:
        app.run()

