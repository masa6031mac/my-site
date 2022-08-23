from flask import Flask,render_template
import socket

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/userlist')
def user_list():
    users = [
        'Taro','jiro','Saburo','Shiro','Hanako','Masa'
    ]
    is_login = False
    host = socket.gethostname()
    my_host = "MasahironoMacBook-Pro.local"

    if host == my_host:
        return render_template('userlist.html', host=host,users=users, is_login=is_login)
    else:
        return render_template('index.html', host=host,users=users, is_login=is_login)

if __name__ == '__main__':

    host = socket.gethostname()
    my_host = "MasahironoMacBook-Pro.local"

    if host == my_host:
        app.run(debug=True)
    else:
        app.run()

