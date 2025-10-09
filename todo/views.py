from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignupForm, TaskForm
from .models import Task
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('/home/')
        else:
            form = TaskForm()

    list = Task.objects.filter(user = request.user).order_by('-deadline')
    return render(request, 'index.html', {'form': form, 'list': list})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')            
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form':form,})
