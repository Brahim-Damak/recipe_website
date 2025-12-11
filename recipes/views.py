from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Recipe, Category
from .api_service import MealDBAPI

def home(request):
    """Home page with random recipes"""
    recipes = []
    for _ in range(6):
        meal_data = MealDBAPI.get_random_recipe()
        if meal_data:
            recipe = MealDBAPI.save_recipe_to_db(meal_data)
            recipes.append(recipe)
    
    categories = MealDBAPI.get_categories()
    
    context = {
        'recipes': recipes,
        'categories': categories[:8],
    }
    return render(request, 'recipes/home.html', context)

def search(request):
    """Search recipes"""
    query = request.GET.get('q', '')
    recipes = []
    
    if query:
        recipes = Recipe.objects.filter(name__icontains=query)
        
        if not recipes:
            meals = MealDBAPI.search_by_name(query)
            if meals:
                for meal in meals:
                    recipe = MealDBAPI.save_recipe_to_db(meal)
                    recipes.append(recipe)
    
    context = {
        'recipes': recipes,
        'query': query,
    }
    return render(request, 'recipes/search.html', context)

def recipe_detail(request, meal_id):
    """Recipe detail page"""
    recipe = Recipe.objects.filter(meal_id=meal_id).first()
    
    if not recipe:
        meal_data = MealDBAPI.get_recipe_by_id(meal_id)
        if meal_data:
            recipe = MealDBAPI.save_recipe_to_db(meal_data)
    
    if not recipe:
        return render(request, 'recipes/404.html', status=404)
    
    context = {
        'recipe': recipe,
    }
    return render(request, 'recipes/detail.html', context)

def category_list(request):
    """List all categories"""
    categories = MealDBAPI.get_categories()
    
    context = {
        'categories': categories,
    }
    return render(request, 'recipes/categories.html', context)

def category_recipes(request, category_name):
    """Show recipes in a category"""
    meals = MealDBAPI.filter_by_category(category_name)
    recipes = []
    
    for meal in meals:
        meal_data = MealDBAPI.get_recipe_by_id(meal['idMeal'])
        if meal_data:
            recipe = MealDBAPI.save_recipe_to_db(meal_data)
            recipes.append(recipe)
    
    context = {
        'recipes': recipes,
        'category': category_name,
    }
    return render(request, 'recipes/category_recipes.html', context) 
