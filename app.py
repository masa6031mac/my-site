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
    return render_template('userlist.html', users=users)

if __name__ == '__main__':
    app.run()