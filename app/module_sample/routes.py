from flask import get_flashed_messages, render_template
from flask.ext.login import current_user

from . import module_sample

@module_sample.route('/')
def index():
    message = get_flashed_messages(False, ['message'])
    email = 'guest'
    return render_template('skelton.html', user=current_user, message=message)

