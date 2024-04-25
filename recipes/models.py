from django.db import models
import json

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default="")
    recipe_json = models.JSONField(default=dict) 

    def __str__(self):
        return self.title

    def ingredient_count(self):
        return len(self.recipe_json.get('ingredients', []))

    def step_count(self):
        return len(self.recipe_json.get('steps', []))

    def save(self, *args, **kwargs):
        # Guarda el campo JSON como un diccionario si se pasa como cadena
        if isinstance(self.recipe_json, str):
            self.recipe_json = json.loads(self.recipe_json)
        super().save(*args, **kwargs)
    
class Unit(models.Model):
    unit = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.unit