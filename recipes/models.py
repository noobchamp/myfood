from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default='')
    ingredients = models.TextField(default='')
    instructions = models.TextField(default='')
    image = models.ImageField(upload_to='recipe_images/', default='default_image.jpg')

    def __str__(self):
        return self.title