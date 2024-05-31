from django.test import TestCase
from recipe.models import Recipe, Category

class RecipeModelTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Desserts")
        self.recipe_data = {
            'title': 'Chocolate Cake',
            'description': 'Delicious chocolate cake.',
            'instructions': 'Mix ingredients, bake at 350F for 30 minutes.',
            'ingredients': 'Flour, sugar, cocoa powder, baking powder, eggs, milk, butter',
            'category': self.category
        }

    def test_recipe_creation(self):
        recipe = Recipe.objects.create(**self.recipe_data)
        self.assertEqual(Recipe.objects.count(), 1)
        self.assertEqual(recipe.title, 'Chocolate Cake')
        self.assertEqual(recipe.description, 'Delicious chocolate cake.')
        self.assertEqual(recipe.instructions, 'Mix ingredients, bake at 350F for 30 minutes.')
        self.assertEqual(recipe.ingredients, 'Flour, sugar, cocoa powder, baking powder, eggs, milk, butter')
        self.assertEqual(recipe.category, self.category)

    def test_recipe_str_method(self):
        recipe = Recipe.objects.create(**self.recipe_data)
        self.assertEqual(str(recipe), 'Chocolate Cake')

    def test_category_name(self):
        category = Category.objects.get(name="Desserts")
        self.assertEqual(category.name, "Desserts")

    def test_recipe_instructions_exist(self):
        recipe = Recipe.objects.create(**self.recipe_data)
        self.assertTrue(recipe.instructions)

    def test_category_count(self):
        category_count = Category.objects.count()
        self.assertEqual(category_count, 1)
