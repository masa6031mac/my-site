from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/userlist')
def user_list():
    users = [
        'Taro','jiro','Saburo','Shiro'
    ]
    is_login = False
    return render_template('userlist.html', users=users, is_login=is_login)

if __name__ == '__main__':
    app.run()