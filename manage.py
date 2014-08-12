#!/usr/bin/env python
import os
if os.path.exists('.env'):
    print('Import environment from .env')
    for line in open('.env'):
        kv = line.strip().split('=')
        if len(kv) == 2:
            os.environ[kv[0].strip()] = kv[1].strip()

from flask.ext.script import Manager

from app import create_app, db
from app.models import User

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)


@manager.command
def adduser(email):
    from getpass import getpass
    password = getpass()
    password2 = getpass(prompt='Confirm:')
    if password != password2:
        import sys
        sys.exit('passwords do not match')

    db.create_all()
    user = User(email=email, password=password)
    user.save()
    print('User {0} was registered.'.format(email))


if __name__ == '__main__':
    manager.run()

