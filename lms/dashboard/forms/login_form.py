from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ValidationError


class LoginForm(AuthenticationForm):
  
  pass
    # email = forms.CharField(max_length=100, required = True)
    # result = authenticate(username = user.username, password = password)
    # if(result is not None):
    #     login(self.request, result)
    #     print(result)
        # return result






