import unittest
from app.model.user_model import User
from app.model.application import Application


class TestUseUserAuthentication(unittest.TestCase):
    def setUp(self):
        self.user = User('philo', 'pass', 'Philip')
        self.app = Application()

    def test_user_added_to_dictionary_when_created(self):
        self.assertTrue(self.app.register_user(self.user))

    def test_user_exists_in_dictionary(self):
        self.app.users = {'philo': self.user}
        self.assertFalse(self.app.register_user(self.user))

    def test_user_is_registered(self):
        self.app.users = {'philo': self.user}
        self.assertTrue(self.app.does_user_exist('philo'))

    def test_user_has_correct_password(self):
        self.app.users = {'philo': self.user}
        self.assertTrue(self.app.login_user('philo', 'pass'))

    def test_user_entered_wrong_password(self):
        self.app.users = {'philo': self.user}
        self.assertFalse(self.app.login_user('philo', 'pass123'))
