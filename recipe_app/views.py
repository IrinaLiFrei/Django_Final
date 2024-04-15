from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe, Category
from .forms import RecipeForm


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
    return render(request, 'recipe_app/recipe_detail.html', {'recipe': recipe})


def categories(request, category):
    recipes = Recipe.objects.filter(category__category=category)
    return render(request, 'recipe_app/categories.html', {'recipes': recipes, 'category': category})


#
# def register(request):
#     return render(request, 'register.html')
# https://pressanybutton.ru/post/sajt-na-django/django-32-forma-registracii/
#
# def login(request):
#     return render(request, 'login.html')
# https://pressanybutton.ru/post/sajt-na-django/django-31-forma-avtorizacii-i-knopka-vyhoda/
#
#
# def logout(request):
#     return render(request, 'logout.html')
#
# @login_required(login_url='/login/')
# def profile(request):
#     return render(request, 'profile.html')


# def edit_recipe(request):
#     return render(request, 'edit_recipe.html')
#
#
# def recipe_list(request):
#     recipes = Recipe.objects.all()
#     return render(request, 'recipe_list.html', {'recipes': recipes})


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
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm()
        message = f'Добавьте свой любимый рецепт.'
    return render(request, 'recipe_app/add_recipe.html', {'form': form, 'message': message})

# def edit_recipe(request, product_id):
#     product = get_object_or_404(models.Product, pk=product_id)
#     if request.method == 'POST':
#         form = EditProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             p        if form.is_valid():
#             recipe.dish_name = form.cleaned_data['dish_name']
#             recipe.description = form.cleaned_data['description']
#             recipe.ingredients = form.cleaned_data['ingredients']
#             recipe.cooking_steps = form.cleaned_data['cooking_steps']
#             recipe.cooking_time = form.cleaned_data['cooking_time']
#             recipe.image = form.cleaned_data['image']
#             recipe.author = form.cleaned_data['author']
#             recipe.created_at = form.cleaned_data['created_at']
#             recipe.save()
#             message = f'Рецепт {recipe.dish_name} добавлен.'
#             if 'image' in request.FILES:
#                 recipe.image = request.FILES['image']
#                 recipe.save()
#
#     else:
#         initial_data = {
#             'name': product.name,
#             'description': product.description,
#             'price': product.price,
#             'stock': product.stock,
#             'entry_date': product.entry_date,
#             'image': product.product_image,
#         }
#         form = EditProductForm(initial=initial_data)
#         message = f'Внесите изменения в товар {product.id} - {product.name}.'
#     return render(request, 'shop_app/edit_form.html', {'form': form, 'message': message})
