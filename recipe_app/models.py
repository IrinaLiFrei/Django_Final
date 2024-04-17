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

