from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required = True)
    last_name = forms.CharField(max_length=100, required = True)
    email = forms.CharField(max_length=100, required = True)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1" , "password2"]




