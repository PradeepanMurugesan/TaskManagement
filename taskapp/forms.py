from django import forms
from .models import Task, TaskUpdate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'deadline', 'priority', 'assign_to']
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'})
        }
        
class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = TaskUpdate
        fields = ['task_status', 'remarks']


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']