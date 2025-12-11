from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('recipe/<str:meal_id>/', views.recipe_detail, name='detail'),
    path('categories/', views.category_list, name='categories'),
    path('category/<str:category_name>/', views.category_recipes, name='category_recipes'),
] 
