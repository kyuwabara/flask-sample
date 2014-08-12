from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy

from config import config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    if not app.config['DEBUG'] and not app.config['TESTING']:
        # configure for production
        pass

    db.init_app(app)
    login_manager.init_app(app)

    from .module_sample import module_sample as sample_blueprint
    app.register_blueprint(sample_blueprint)
    app.register_blueprint(sample_blueprint, url_prefix='/subdir')

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')


    return app

