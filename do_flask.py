from flask import Flask, request, render_template

do_flask = Flask(__name__)


@do_flask.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@do_flask.route('/signin', methods=['GET'])
def sign_form():
    return render_template('form.html')


@do_flask.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    # 需要从request对象读取表单内容：
    if username == 'admin' and password == 'password':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)


if __name__ == '__main__':
    do_flask.run()