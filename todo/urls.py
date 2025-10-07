from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm

urlpatterns = [
    path('', views.signup, name="signup"),
    path('home/', views.home, name="home"),
    path('login/', auth_views.LoginView.as_view(authentication_form= LoginForm), name='login'),
    path('signup/', views.signup, name="signup")
]