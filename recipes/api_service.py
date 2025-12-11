import requests
from .models import Recipe, Ingredient, Category

class MealDBAPI:
    BASE_URL = "https://www.themealdb.com/api/json/v1/1"
    
    @staticmethod
    def search_by_name(name):
        """Search recipes by name"""
        url = f"{MealDBAPI.BASE_URL}/search.php"
        response = requests.get(url, params={'s': name})
        if response.status_code == 200:
            return response.json().get('meals', [])
        return []
    
    @staticmethod
    def get_recipe_by_id(meal_id):
        """Get recipe details by ID"""
        url = f"{MealDBAPI.BASE_URL}/lookup.php"
        response = requests.get(url, params={'i': meal_id})
        if response.status_code == 200:
            meals = response.json().get('meals', [])
            return meals[0] if meals else None
        return None
    
    @staticmethod
    def get_random_recipe():
        """Get a random recipe"""
        url = f"{MealDBAPI.BASE_URL}/random.php"
        response = requests.get(url)
        if response.status_code == 200:
            meals = response.json().get('meals', [])
            return meals[0] if meals else None
        return None
    
    @staticmethod
    def get_categories():
        """Get all categories"""
        url = f"{MealDBAPI.BASE_URL}/categories.php"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json().get('categories', [])
        return []
    
    @staticmethod
    def filter_by_category(category):
        """Filter recipes by category"""
        url = f"{MealDBAPI.BASE_URL}/filter.php"
        response = requests.get(url, params={'c': category})
        if response.status_code == 200:
            return response.json().get('meals', [])
        return []
    
    @staticmethod
    def save_recipe_to_db(meal_data):
        """Save recipe data to database"""
        recipe, created = Recipe.objects.update_or_create(
            meal_id=meal_data['idMeal'],
            defaults={
                'name': meal_data['strMeal'],
                'category': meal_data.get('strCategory', ''),
                'area': meal_data.get('strArea', ''),
                'instructions': meal_data.get('strInstructions', ''),
                'thumbnail': meal_data.get('strMealThumb', ''),
                'youtube': meal_data.get('strYoutube', ''),
                'tags': meal_data.get('strTags', ''),
            }
        )
        
        # Save ingredients
        if created:
            for i in range(1, 21):
                ingredient = meal_data.get(f'strIngredient{i}')
                measure = meal_data.get(f'strMeasure{i}')
                if ingredient and ingredient.strip():
                    Ingredient.objects.create(
                        recipe=recipe,
                        name=ingredient.strip(),
                        measure=measure.strip() if measure else ''
                    )
        
        return recipe 