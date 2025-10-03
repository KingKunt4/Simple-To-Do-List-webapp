from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    model = User
    fields = ('username', 'email', 'password1', 'password2',)
    username= forms.CharField(widget= forms.TextInput(attrs={'id':'fields'}))
    email= forms.CharField(widget= forms.EmailInput(attrs={'id':'fields'}))
    password1= forms.CharField(widget= forms.PasswordInput(attrs={'id':'fields'}))
    password2= forms.CharField(widget= forms.PasswordInput(attrs={'id':'fields'}))

class LoginForm(AuthenticationForm):
    model = User
    fields = ('username', 'password') 