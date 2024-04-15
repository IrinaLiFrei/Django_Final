from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.category}'


class Recipe(models.Model):
    dish_name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    ingredients = models.TextField(max_length=1000)
    cooking_steps = models.TextField(max_length=5000)
    cooking_time = models.IntegerField()
    image = models.ImageField(upload_to='recipe_images')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.dish_name}  {self.category} {self.description} {self.ingredients} {self.cooking_steps} {self.cooking_time} {self.image} {self.author}'

    # @property
    # def ingredients_list(self):
    #     ingredients_list = str(self.ingredients.split('\n').split(','))
    #     for ingredient in ingredients_list:
    #         return f'{ingredient}

    #     # ingredients_list = [ingredient.strip() for ingredient in self.ingredients.split(',').split('\n') if ingredient.strip()]
    #     return ingredients_list
    #
    # @property
    # def cooking_steps_list(self):
    #     cooking_steps_list = [step.strip() for step in self.cooking_steps.split('\n') if step.strip()]
    #     return cooking_steps_list


# class RecipeCategory(models.Model):
#     recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f'{self.recipe} {self.category}'

# class Ingredient(models.Model):
#     name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.name
