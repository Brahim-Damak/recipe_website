from django.db import models

class Category(models.Model):
    category_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    thumbnail = models.URLField(blank=True)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name

class Recipe(models.Model):
    meal_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    instructions = models.TextField()
    thumbnail = models.URLField()
    youtube = models.URLField(blank=True, null=True)
    tags = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')
    name = models.CharField(max_length=100)
    measure = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.measure} {self.name}"