from django.contrib import admin
from .models import Recipe, Category



@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('dish_name', 'description', 'author', 'created_at')
    readonly_fields = ['created_at']
    fieldsets = [
        (None,
         {'classes': ['wide'],
          'fields': ['dish_name', 'description'],
          }
         ),
        ('Details',
         {'fields': ['ingredients', 'cooking_steps', 'cooking_time'],
          }
         ),
        ('Author',
         {'fields': ['author'],
          }
         ),
        ('Other details',
         {'description': 'Views',
          'fields': ['image', 'category', 'created_at'],
          }
         ),
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)


# @admin.register(RecipeCategory)
# class RecipeCategoryAdmin(admin.ModelAdmin):
#     list_display = ('recipe', 'category',)


