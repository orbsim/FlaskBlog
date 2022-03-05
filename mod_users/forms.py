import email
from click import password_option
from flask_wtf import FlaskForm
from wtforms.fields import EmailField
from wtforms import PasswordField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = EmailField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    