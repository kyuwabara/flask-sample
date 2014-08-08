#!/usr/bin/env python
import os
if os.path.exists('.env'):
    print('Import environment from .env')
    for line in open('.env'):
        kv = line.strip().split('=')
        if len(kv) == 2:
            os.environ[kv[0].strip()] = kv[1].strip()

from app import create_app
from flask.ext.script import Manager

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

if __name__ == '__main__':
    manager.run()

