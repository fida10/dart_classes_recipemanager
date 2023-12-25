""" 
Question 6: Recipe Manager

Description:

Create a class called RecipeManager. It should have the following attributes and methods:

Attributes: recipe_book_name (string), recipes (dictionary with recipe names as keys and lists of ingredients as values).

Methods:

add_recipe(recipe_name, ingredients): Adds a new recipe.

remove_recipe(recipe_name): Removes a recipe.

get_ingredients(recipe_name): Returns a list of ingredients for the specified recipe.
"""

class RecipeManager: 
    def __init__(self, recipe_listing):
        self.recipe_listing = recipe_listing
        self.recipes = {}
    
    def add_recipe(self, recipe_name, recipe_ingredients):
        self.recipes[recipe_name] = recipe_ingredients
    
    def remove_recipe(self, recipe_name):
        self.recipes.pop(recipe_name)

    def get_ingredients(self, recipe_name):
        return self.recipes[recipe_name]
