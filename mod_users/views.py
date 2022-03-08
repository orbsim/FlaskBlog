from flask import flash, render_template, request
from app import db
from . import users
from .forms import RegisterForm
from .models import User
from sqlalchemy.exc import IntegrityError

@users.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST':
        if not form.validate_on_submit():
            return render_template('users/register.html', form=form)
        if form.password.data != form.confirm_password.data:
            error_msg = 'Password and confirm password does not match.'
            form.password.errors.append(error_msg)
            form.confirm_password.errors.append(error_msg)
            return render_template('users/register.html', form=form)

        old_user = User.query.filter(User.email.ilike(form.email.data)).first()
        if old_user:
            flash('Email is in use.', 'error')
            return render_template('users/register.html', form=form)

        new_user = User()
        new_user.full_name = form.full_name.data
        new_user.email = form.email.data
        new_user.set_password(form.password.data)
        try:
            db.session.add(new_user)
            db.session.commit()
            flash('You created your account successfully')
        except IntegrityError:
            db.session.rollback()
            flash('Email in is use.', 'error')

    return render_template('users/register.html', form=form)
