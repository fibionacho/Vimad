from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    email = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'ej. usuario@dominio.es','oninput' : 'checkValid(event)', 'spellcheck':'false','required':'required'}),
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'ej. usuario','oninput' : 'checkValid(event)', 'spellcheck':'false','required':'required'}),
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'Tu contraseña','oninput' : 'checkValid(event)', 'type':'password','required':'required'}),
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'Repite tu contraseña','oninput' : 'checkValid(event)', 'type':'password', 'required':'required'}),
    )


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'control','placeholder':'Usuario', 'spellcheck':'false'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'control','placeholder': 'Contraseña','id':'password','type':'password' }))
