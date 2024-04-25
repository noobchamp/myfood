from django.shortcuts import render, redirect
from .models import Recipe, Unit
from .forms import RecipeForm
import json

def recipe_list(request):

    return render(request, 'recipes/recipe_list.html')

def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

def create_recipe(request):
    units = Unit.objects.all()
    units_json = json.dumps([unit.unit for unit in units])  # Convertir unidades a JSON
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            print(form)
            title = form.cleaned_data['title']
            ingredients = form.cleaned_data['ingredients']
            steps = form.cleaned_data['steps']
            
            # Aquí puedes convertir los ingredientes y pasos a un formato JSON si es necesario
            # Por ejemplo, puedes hacer algo como:
            ingredients_json = json.loads(ingredients)
            steps_json = json.loads(steps)
            
            # Luego, guarda los datos en tu modelo Recipe
            recipe = Recipe.objects.create(
                title=title,
                recipe_json={'ingredients': ingredients, 'steps': steps}  # Aquí guardamos los datos como un diccionario JSON
            )
            # Puedes realizar otras acciones, como redirigir a la página de detalles de la receta
            return redirect('recipe_detail', pk=recipe.pk)
        else:
            print(form.errors)
    else:
        form = RecipeForm()
    return render(request, 'recipes/create_recipe.html', {'form': form, 'units': units_json})