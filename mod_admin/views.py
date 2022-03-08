from flask import session, render_template, request, abort, flash
from mod_users.forms import LoginForm
from mod_users.models import User
from . import admin

@admin.route('/')
def index():
    return "Hello from admin Index"

@admin.route('/login/', methods=['GET', 'POST'])
def login():
    if session.get('user_id') is not None:
        return "Your are already logged in"
    form = LoginForm(request.form)
    if request.method == 'POST':
        if not form.validate_on_submit():
            abort(400)
        #user = User.query.filter(User.email == form.email.data).first()
        user = User.query.filter(User.email.ilike(f'{form.email.data}')).first()
        if not user:
            #return "Incorrect Credentials", 400
            flash('Incorrect Credentials', category='warning')
            return render_template('admin/login.html', form=form)
        if not user.check_password(form.password.data):
            #return "Incorrect Credentials", 400
            flash('Incorrect Credentials', category='error')
            return render_template('admin/login.html', form=form)
        if session.get('user_id') is not None:
            return "Your are already logged in"
        if not user.is_admin():
            return "You do not have permission to login "

        session['email'] = user.email
        session['user_id'] = user.id
        session['role'] = user.role
        return "Logined in successfully"

        #print(f"Form is validated? {form.validate_on_submit()}")
    return render_template('admin/login.html', form=form)