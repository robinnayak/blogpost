from django import forms
from django.forms.models import ModelForm
from .models import Author, Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class AuthorForm(ModelForm):
    
    class Meta:
        model = Author
        fields = ("name","email","desc","profile")


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email']


class LoginForm (forms.Form):
    username = forms.CharField(label="username", max_length=100)
    password = forms.CharField(widget=forms.PasswordInput,label="password", max_length=50)    