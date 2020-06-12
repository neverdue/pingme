from flask import Flask, render_template

from forms import *
from models import *


app = Flask(__name__)
app.secret_key = "replace this"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://oyeubcfprgkknv:61c161ce0a9f0a2591792d4443083dd3f8e5e24ff3c68ca012b456698623c84e@ec2-34-193-117-204.compute-1.amazonaws.com:5432/d880fut9ik2j31"
db = SQLAlchemy(app)


@app.route('/', methods=["GET", "POST"])
def index():
    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data

        user_object = User.query.filter_by(username=username).first()

        if user_object:
            return "Someone already has registered with that username!"

        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return "Successfully Registered!"
    return render_template("index.html", form=reg_form)


if __name__ == "__main__":
    app.run(debug=True)
