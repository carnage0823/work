from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, URL
import csv
import pandas as pd

# creating a data frame

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

bootstrap = Bootstrap(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# CREATE TABLE
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


db.create_all()

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        # Email doesn't exist or password incorrect.
        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for('index'))
        elif not (user.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('index'))
        else:
            print("login")
            login_user(user)
            return redirect(url_for('add'))


    return render_template("index.html", logged_in=current_user.is_authenticated)

@app.route('/add', methods=["GET", "POST"])
@login_required
def add():
    class CafeForm(FlaskForm):
        emp_name = StringField('full name', validators=[DataRequired()])
        address = StringField("address")
        email = StringField("email")
        phone = IntegerField("phone")
        branch = StringField("branch")
        submit = SubmitField('Submit')

    form = CafeForm()
    if form.validate_on_submit():
        with open("employees-data.csv", mode="a") as csv_file:
            csv_file.write(
                           f"\n{form.emp_name.data},"
                           f"{form.email.data},"
                           f"{form.address.data},"
                           f"{form.phone.data},"
                           f"{form.branch.data},")
        df = pd.read_csv("employees-data.csv")
        print(df.head())
        return redirect(url_for('add'))


    return render_template("add.html", form=form,  logged_in=True)


@app.route('/employees')
def employees():
    with open('employees-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('employees.html', cafes=list_of_rows)


if __name__ == "__main__":
    app.run(debug=True)
