import unittest
from app.model.user_model import User
from app.model.categories import Categories


class TestUserCategory(unittest.TestCase):
    def setUp(self):
        self.user = User('philo', 'pass')
        self.category = Categories('AZXDJSA', 'Chicken')

    def test_user_create_category(self):
        self.assertTrue(self.user.create_user_category(self.category))

    def test_user_category_exists(self):
        self.user.categories = {"AZXDJSA": self.category}
        self.assertFalse(self.user.create_user_category(self.category))

    def test_user_category_exists_by_name(self):
        self.user.categories = {"AZJSA": self.category}
        #self.assertFalse(self.user.create_user_category(self.category))

    def test_correct_category_list_returned_by_id(self):
        self.user.categories = {"AZXDJSA": self.category}
        self.assertEqual(self.user.get_category("AZXDJSA"),
                         self.category)

    def test_none_returned_if_id_is_unknown(self):
        self.assertIsNone(self.user.get_category("ABGDTAD"))

    def test_category_list_is_updated(self):
        self.user.categories = {"AZXDJSA": self.category}
        self.user.update_category("AZXDJSA", 'Beaf')
        self.assertEqual(self.user.get_category("AZXDJSA").name,
                         "Beaf")

    def test_updating_none_existing_categories(self):
        self.assertFalse(self.user.update_category("BDBHGF", "Pork"))

    def test_category_successfully_deleted(self):
        self.user.delete_category("AZXDJSA")
        self.assertEqual(self.user.categories, {})

    def test_false_returned_when_deleting_none_existing_category(self):
        self.assertFalse(self.user.delete_category("AZXDJSA"))


if __name__ == '__main__':
    unittest.main()
