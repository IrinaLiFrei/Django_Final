from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recipe_detail/<int:recipe_id>', views.recipe_detail, name='recipe_detail'),
    path('categories/<str:category>', views.categories, name='categories'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('edit_recipe/<int:recipe_id>', views.edit_recipe, name='edit_recipe'),
    path('register/', views.register_request, name="register"),
]
