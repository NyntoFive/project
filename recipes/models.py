from django.conf import settings
from django.db import models

"""
- Global
  - Ingredients
  - Recipes
-User
  - Ingredients
  - Recipes
    - Ingredients
    - Directions 
"""

class Recipe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    directions = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    quantity = models.CharField(max_length=50) # 1 1/4
    directions = models.TextField(blank=True, null=True)
    unit = models.CharField(max_length=50) # lbs, oz, tsp, cup...
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# class RecipeImage(models.Model):
    # recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    # name = models.CharField(max_length=200)
    # image = models.ImageField(upload_to="images/recipes/")