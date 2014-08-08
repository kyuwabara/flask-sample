from flask import Blueprint

module_sample = Blueprint('module_sample', __name__)

from . import routes

