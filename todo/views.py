from django.shortcuts import render, redirect
from .forms import SignupForm
from .models import Todo
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'index.html',)

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')            
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form':form,})

