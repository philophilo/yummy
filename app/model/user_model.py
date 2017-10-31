class User:
    def __init__(self, username, password, name=None):
        self.username = username
        self.password = password
        self.name = name
        self.categories = dict()

    def create_user_category(self, category):
        if category.id in self.categories.keys():
            return False
        self.categories[category.id] = category
        return True

    def get_category(self, list_id):
        if list_id in self.categories.keys():
            return self.categories[list_id]
        return None

    def update_category(self, list_id, name):
        if list_id in self.categories.keys():
            self.categories[list_id].name = name
            return True
        return False

    def delete_category(self, list_id):
        if list_id in self.categories.keys():
            self.categories.pop(list_id)
            return True
        return False
