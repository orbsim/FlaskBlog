import email
from click import password_option
from flask_wtf import FlaskForm
from wtforms.fields import EmailField, StringField
from wtforms import PasswordField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = EmailField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])


class RegisterForm(FlaskForm):
    full_name = StringField()
    email = EmailField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    confirm_password = PasswordField(validators=[DataRequired()])
    