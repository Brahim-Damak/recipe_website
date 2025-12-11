from django.contrib import admin
from .models import Recipe, Ingredient, Category

class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 1

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'area', 'created_at']
    list_filter = ['category', 'area']
    search_fields = ['name', 'category']
    inlines = [IngredientInline]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category_id']

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ['name', 'measure', 'recipe']
    list_filter = ['recipe'] 
    