from django import forms
from .models import Movies, Categories


class MoviesForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = '__all__'

class CategoriesForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = '__all__'

class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario')
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
