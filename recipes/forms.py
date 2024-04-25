from django import forms

class RecipeForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.Textarea()
    # ingredients = forms.CharField(widget=forms.Textarea)
    # steps = forms.CharField(widget=forms.Textarea)