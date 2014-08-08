import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = 'DevelopmentSecretKey'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'devel.db')


class TestingConfig(Config):
    TESTING = True
    SECRET_KEY = 'TestingSecretKey'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
            'sqlite:///' + os.path.join(basedir, 'prod.db')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
    }

