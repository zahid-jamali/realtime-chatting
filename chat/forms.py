from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from . import models

class CustomUserCreationFrom(UserCreationForm):
    class Meta:
        model=models.CustomUser
        fields=['name', 'email', 'phone']


class loginForm(AuthenticationForm):
    # username.widget=forms.EmailInput(attrs={"autofocus": True}))
    class Meta:
        model=models.CustomUser