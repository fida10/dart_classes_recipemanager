import unittest
from src.ans import RecipeManager

class TestRecipeManager(unittest.TestCase):
    def setUp(self):
        self.recipe_manager = RecipeManager("Healthy Eats")

    def test_add_recipe(self):
        self.recipe_manager.add_recipe(
            "Salad", ["Lettuce", "Tomato", "Cucumber"])
        self.assertIn("Salad", self.recipe_manager.recipes)
        self.assertEqual(self.recipe_manager.recipes["Salad"], [
                        "Lettuce", "Tomato", "Cucumber"])

    def test_remove_recipe(self):
        self.recipe_manager.add_recipe("Soup", ["Broth", "Carrots", "Chicken"])
        self.recipe_manager.remove_recipe("Soup")
        self.assertNotIn("Soup", self.recipe_manager.recipes)

    def test_get_ingredients(self):
        self.recipe_manager.add_recipe("Smoothie", ["Banana", "Milk", "Honey"])
        expected_ingredients = ["Banana", "Milk", "Honey"]
        self.assertEqual(self.recipe_manager.get_ingredients(
            "Smoothie"), expected_ingredients)


if __name__ == '__main__':
    unittest.main()
