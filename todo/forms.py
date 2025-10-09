from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Task

class SignupForm(UserCreationForm):
    model = User
    fields = ('username', 'email', 'password1', 'password2',)
    username= forms.CharField(widget= forms.TextInput(attrs={'class':'fields'}))
    email= forms.CharField(widget= forms.EmailInput(attrs={'class':'fields'}))
    password1= forms.CharField(widget= forms.PasswordInput(attrs={'class':'fields'}))
    password2= forms.CharField(widget= forms.PasswordInput(attrs={'class':'fields'}))

class LoginForm(AuthenticationForm):
    model = User
    fields = ('username', 'password')
    username = forms.CharField(widget= forms.TextInput(attrs={'class': 'fields'}))
    password = forms.CharField(widget= forms.PasswordInput(attrs={'class': 'fields'}))

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title','deadline', 'complete',)
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date', 'class':'datefield'}),
            'title': forms.TextInput(attrs={'class': 'fields'}),
            'complete': forms.CheckboxInput(attrs={'class': 'chkbox'})
            }