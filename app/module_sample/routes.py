from flask import render_template

from . import module_sample

@module_sample.route('/')
def index():
    return render_template('skelton.html')

