class Categories():
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.recipes = {}

    def create_recipe(self, recipe):
        if recipe.id in self.recipes.keys():
            return False
        self.recipes[recipe.id] = recipe
        return True

    def get_recipe(self, list_id):
        if list_id in self.recipes.keys():
            return self.recipes[list_id]
        return None

    def update_recipe(self, list_id, name, ingredients, date):
        if list_id in self.recipes.keys():
            self.recipes[list_id].name = name
            self.recipes[list_id].ingredients = ingredients
            self.recipes[list_id].date = date
            return True
        return False

    def delete_recipe(self, list_id):
        if list_id in self.recipes.keys():
            self.recipes.pop(list_id)
            return True
        return False


class Recipes():

    def __init__(self, list_id, name, ingredients, date):
        self.id = list_id
        self.name = name
        self.ingredients = ingredients
        self.date = date
