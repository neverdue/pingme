from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, current_user

from forms import *
from models import *


app = Flask(__name__)
app.secret_key = "replace this"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://oyeubcfprgkknv:61c161ce0a9f0a2591792d4443083dd3f8e5e24ff3c68ca012b456698623c84e@ec2-34-193-117-204.compute-1.amazonaws.com:5432/d880fut9ik2j31"
db = SQLAlchemy(app)

login = LoginManager(app)
login.init_app(app)

@login.user_loader
def load_user(id):

    return User.query.get(int(id))


@app.route('/', methods=["GET", "POST"])
def index():
    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data

        hashed_password = pbkdf2_sha256.hash(password)

        user = User(username=username, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template("index.html", form=reg_form)


@app.route('/login', methods = ["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user_object = User.query.filter_by(username=login_form.username.data).first()
        login_user(user_object)
        return redirect(url_for('chat'))

    return render_template("login.html", form=login_form)

@app.route('/chat', methods = ["GET", "POST"])
def chat():

    if not current_user.is_authenticated:
        return "Please login before trying to access this page"

    return "Ping Me!"

@app.route('/logout', methods = ["GET"])
def logout():

    logout_user()
    return "Logged you out! Goodbye!"


if __name__ == "__main__":
    app.run(debug=True)
