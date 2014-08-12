from datetime import datetime

from flask.ext.login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from . import db, login_manager


class MyMixin(object):
    id = db.Column(db.Integer, primary_key=True)

    def save(self):
        if 'updated_at' in dir(self):
            self.updated_at = datetime.now()
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class User(UserMixin, db.Model, MyMixin):
    __tablename__ = 'users'

    email = db.Column(db.String(64), nullable=False, unique=True, index=True)
    password_hash = db.Column(db.String(128))
    registered_at = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

    @property
    def password(self):
        raise AttributeError('unreadable.')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

