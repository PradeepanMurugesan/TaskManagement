from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from .forms import TaskForm, TaskUpdateForm, UserForm
from .models import Task, TaskUpdate, UserDetail
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserDetail.objects.create(user=user)  
            auth_login(request, user)
            return redirect('login')
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('task_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('login')

def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasklist.html', {'tasks': tasks})

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'addtask.html', {'form': form, 'action': 'Add'})

@login_required
def update_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id,user=request.user)
    
    if request.method == 'POST':
        form = TaskUpdateForm(request.POST)
        if form.is_valid():
            task_update = form.save(commit=False)
            task_update.user = request.user  
            task_update.task = task
            task_update.save()
            return redirect('task_list')
    else:
        form = TaskUpdateForm()
    
    return render(request, 'updatetask.html', {'form': form})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'delete_task.html', {'task': task})

@login_required
def completed_tasks(request):
    completed_updates = TaskUpdate.objects.filter(user=request.user, task_status='completed')
    ongoing_updates = TaskUpdate.objects.filter(user=request.user, task_status='ongoing')
    dropped_updates = TaskUpdate.objects.filter(user=request.user, task_status='dropped')

    return render(request, 'completed_tasks.html', {
        'completed_updates': completed_updates,
        'ongoing_updates': ongoing_updates,
        'dropped_updates': dropped_updates
    })

