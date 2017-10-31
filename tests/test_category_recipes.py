import unittest
from app.model.categories import Categories, Recipes


class TestCategoryItems(unittest.TestCase):

    def setUp(self):
        self.category = Categories('XZBNVLK', 'Beaf recipe')

    def test_user_can_create_recipe(self):
        item = Recipes('XZBNVLK', 'Beaf recipe',
                       ['Beaf', 'kachumabli', 'curry'], '2017-10-29')
        self.assertTrue(self.category.create_recipe(item))

    def test_recipe_already_exists_in_category(self):
        recipe = Recipes('XZBNVLK', 'Beaf recipe',
                         ['Beaf', 'kachumabli', 'curry'], '2017-10-29')
        self.category.recipes = {'XZBNVLK': recipe}
        self.assertFalse(self.category.create_recipe(recipe))

    def test_recipe_returned_when_id_is_specified(self):
        recipe = Recipes('XZBNVLK', 'Beaf recipe',
                         ['Beaf', 'kachumabli', 'curry'], '2017-10-29')
        self.category.recipes = {'XZBNVLK': recipe}
        self.assertEqual(self.category.get_recipe(recipe.id), recipe)

    def test_none_is_returned_when_recipe_is_not_found_by_id(self):
        self.assertIsNone(self.category.get_recipe("VBDHJFS"))

    def test_recipe_in_category_is_updated(self):
        recipe = Recipes('XZBNVLK', 'Beaf recipe',
                         ['Beaf', 'kachumabli', 'curry'], '2017-10-29')
        self.category.recipes = {'XZBNVLK': recipe}
        self.category.update_recipe('XZBNVLK', 'Ugandan Beaf recipe',
                                    ['Beaf', 'kachumabli', 'curry'],
                                    '2017-10-29')
        self.assertEqual(self.category.get_recipe('XZBNVLK').name,
                         'Ugandan Beaf recipe')

    def test_when_category_for_update_is_missing(self):
        self.assertFalse(self.category.update_recipe(
            'AGHGJC', 'Kampala', ['Beaf', 'kachumabli', 'curry'],
            '2017-10-29'))

    def test_category_successfully_updated(self):
        recipe = Recipes('XZBNVLK', 'Beaf recipe',
                         ['Beaf', 'kachumabli', 'curry'], '2017-10-29')
        self.category.recipes = {'XZBNVLK': recipe}
        self.category.delete_recipe('XZBNVLK')
        self.assertEqual(self.category.recipes, {})

    def test_non_exiting_recipe_cannot_be_deleted(self):
        self.assertFalse(self.category.delete_recipe("HJJJFG"))


if __name__ == "__main__":
    unittest.main()
