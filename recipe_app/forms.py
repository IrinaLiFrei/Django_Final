from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


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


class ImageForm(forms.Form):
    image = forms.ImageField(required=False)


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, max_length=150, label='E-mail', widget=forms.TextInput(attrs={'class': 'email-input',
                                                                                          'style': 'margin-bottom: 10px;', }))
    username = forms.CharField(label='Имя пользователя', max_length=150, widget=forms.TextInput(attrs={'class': 'user-input',
                                                                                       'style': 'margin-bottom: 10px;', }))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'pass-input',
                                                                                  'style': 'margin-bottom: 10px;', }))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'pass-input',
                                                                                            'style': 'margin-bottom: 15px;', }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150, label='Имя пользователя', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите имя пользователя',
        'style': 'margin-bottom: 10px;',
        })
    )
    password = forms.CharField(max_length=128, label='Пароль', widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите пароль',
            'style': 'margin-bottom: 10px;',
        })
    )

    class Meta:
        model = User
        fields = ['username', 'password']
