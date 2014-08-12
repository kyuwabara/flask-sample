from flask import get_flashed_messages, render_template, current_app, request, redirect, url_for, flash

from flask.ext.login import login_user, logout_user, login_required
from ..models import User
from . import auth
from .forms import LoginForm

@auth.route('/login', methods=['GET', 'POST'])
def login():
    message = get_flashed_messages(False, ['message'])
    if not current_app.config['DEBUG'] and \
            not current_app.config['TESTING'] and \
            not request.is_secure:
        return redirect(url_for('.login', _external=True, _schema='https'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.verify_password(form.password.data):
            flash('Invalid email or password', category='message')
            return redirect(url_for('.login'))
        login_user(user, form.remember.data)
        return redirect('/subdir')

    return render_template('login.html', form=form, message=message)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('LOG OUT', category='message')
    return redirect(url_for('module_sample.index'))

