class User:
    def __init__(self, username, password, name=None):
        self.username = username
        self.password = password
        self.name = name
        self.categories = dict()

    def check_category_id(self, cat):
        if cat.id in self.categories.keys():
            return False
        return True

    def check_category_name(self, cat):
        for cat_obj in self.categories.values():
            if cat.name == cat_obj.name:
                found = list(self.categories.keys())[list(self.categories.values()).index(cat)]
                return found
        return False

    def create_user_category(self, category):
        if not self.check_category_id(category):
            return False
        found_category_key = self.check_category_name(category)
        if not found_category_key:
            self.categories[category.id] = category
            return True
            """
        else:
            print(found_category_key, ";;;;")
            self.categories[found_category_key].append(category)
            print(self.categories)
            """
        self.categories[category.id] = category
        return True
        """
        for cat_obj in self.categories.values():
            print("..><", cat_obj.name)
            if category.name == cat_obj.name:
                cat_id = list(self.categories.keys())[list(self.categories.values()).index(category)]
                print("----", cat_id)

        if category.id in self.categories.keys():
            # TODO create a list when they are many
            print("here")
            return False
        self.categories[category.id] = [category]
        return True
        """

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
