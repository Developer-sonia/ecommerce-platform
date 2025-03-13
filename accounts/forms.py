from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignUpFrom(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        field = ['username', 'email', 'password1', 'password2' ]