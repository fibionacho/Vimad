from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'control','placeholder':'Usuario', 'spellcheck':'false'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'control','placeholder': 'Contraseña','id':'password','type':'password' }))
