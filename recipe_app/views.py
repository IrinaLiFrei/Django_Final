from datetime import datetime

from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404
from .models import Recipe, Category
from .forms import RecipeForm, UserRegistrationForm, CustomAuthenticationForm


def index(request):
    if Recipe.objects.count() > 5:
        random_recipes = Recipe.objects.order_by('?')[:5]
    else:
        random_recipes = Recipe.objects.all()
    context = {
        'title': 'Главная',
        'random_recipes': random_recipes,
    }
    return render(request, 'recipe_app/index.html', context)


def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    message = ''
    return render(request, 'recipe_app/recipe_detail.html', {'recipe': recipe, 'message': message})


def categories(request, category):
    recipes = Recipe.objects.filter(category__category=category)
    return render(request, 'recipe_app/categories.html', {'recipes': recipes, 'category': category})


def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            dish_name = form.cleaned_data['dish_name']
            description = form.cleaned_data['description']
            ingredients = form.cleaned_data['ingredients']
            cooking_steps = form.cleaned_data['cooking_steps']
            cooking_time = form.cleaned_data['cooking_time']
            image = form.cleaned_data['image']
            author = form.cleaned_data['author']
            category_name = form.cleaned_data['category_name']
            category, created = Category.objects.get_or_create(category=category_name)
            recipe = Recipe(dish_name=dish_name,
                            description=description,
                            ingredients=ingredients,
                            cooking_steps=cooking_steps,
                            cooking_time=cooking_time,
                            image=image, author=author,
                            category=category,
                            created_at=datetime.now())
            recipe.save()
            message = f'Рецепт {recipe.dish_name} добавлен в базу данных.'
            if 'image' in request.FILES:
                recipe.image = request.FILES['image']
                recipe.save()
            return render(request, 'recipe_app/recipe_detail.html', {'recipe': recipe, 'message': message})
    else:
        form = RecipeForm()
        message = f'Добавьте свой любимый рецепт.'
        return render(request, 'recipe_app/add_recipe.html', {'form': form, 'message': message})


def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe.dish_name = form.cleaned_data['dish_name']
            recipe.description = form.cleaned_data['description']
            recipe.ingredients = form.cleaned_data['ingredients']
            recipe.cooking_steps = form.cleaned_data['cooking_steps']
            recipe.cooking_time = form.cleaned_data['cooking_time']
            recipe.author = form.cleaned_data['author']
            recipe.created_at = datetime.now()
            if 'image' in request.FILES:
                recipe.image = request.FILES['image']
            recipe.save()
            message = f'Рецепт {recipe.dish_name} изменён.'
            return render(request, 'recipe_app/recipe_detail.html', {'recipe': recipe, 'message': message})
    else:
        initial_data = {
            'dish_name': recipe.dish_name,
            'description': recipe.description,
            'ingredients': recipe.ingredients,
            'cooking_steps': recipe.cooking_steps,
            'cooking_time': recipe.cooking_time,
            'image': recipe.image,
            'author': recipe.author,
            'created_at': recipe.created_at,
        }
        form = RecipeForm(initial=initial_data)
    message = f'Внесите изменения в рецепт {recipe.dish_name}.'
    return render(request, 'recipe_app/edit_recipe.html', {'form': form, 'message': message})


def register_request(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True
            user.is_superuser = False
            user.save()
            return render(request, 'registration/login.html', {'form': form})
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})



