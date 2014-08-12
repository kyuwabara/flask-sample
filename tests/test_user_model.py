import unittest

from app import create_app, db
from app.models import User, load_user


class UserModelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_setter(self):
        user = User(password='kuwa')
        self.assertTrue(user.password_hash is not None)

    def test_password_getter(self):
        user = User(password='kuwa')
        with self.assertRaises(AttributeError):
            user.password

    def test_verify_password(self):
        user = User(password='kuwa')
        self.assertTrue(user.verify_password('kuwa'))
        self.assertFalse(user.verify_password('bara'))

    def test_random_salts(self):
        user1 = User(password='kuwa')
        user2 = User(password='kuwa')
        self.assertTrue(user1.password_hash != user2.password_hash)

    def test_user_loader(self):
        db.create_all()
        user = User(email='kuwa@example.com', password='kuwa')
        user.save()
        self.assertTrue(load_user(user.id) == user)

