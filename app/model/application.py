import random
import string


class Application:
    users = {}

    def register_user(self, user):
        if user.username in self.users.keys():
            return False
        self.users[user.username] = user
        return True

    def login_user(self, username, password):
        if self.users[username].password == password:
            return True
        return False

    def does_user_exist(self, username):
        if username in self.users.keys():
            return True
        return False

    def get_user(self, username):
        if username in self.users.keys():
            return self.users[username]
        return None

    def generate_random_key(self):
        return ''.join(random.SystemRandom().
                       choice(string.ascii_uppercase +
                              string.digits) for _ in range(10))
