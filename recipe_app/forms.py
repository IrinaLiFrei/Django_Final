from django import forms
from django.contrib.auth.models import User


class RecipeForm(forms.Form):
    dish_name = forms.CharField(required=True, max_length=100)
    description = forms.CharField(required=True, max_length=2000, widget=forms.Textarea)
    ingredients = forms.CharField(required=True, max_length=2000, widget=forms.Textarea)
    cooking_steps = forms.CharField(required=True, widget=forms.Textarea)
    cooking_time = forms.IntegerField(required=True, max_value=1000)
    image = forms.ImageField(required=False)
    author = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    category_name = forms.ChoiceField(choices=[('Холодные закуски', 'Холодные закуски'),
                                               ('Горячие закуски', 'Горячие закуски'),
                                               ('Первые блюда', 'Первые блюда'),
                                               ('Вторые блюда', 'Вторые блюда'),
                                               ('Кондитерские изделия', 'Кондитерские изделия'),
                                               ('Прочее', 'Прочее'),
                                               ])
    # created_at = forms.DateField()


class ImageForm(forms.Form):
    image = forms.ImageField(required=False)
