from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    emp=[
        ('Pradeep','Pradeep'),
        ('Lathish','Lathish'),
        ('Vicky','Vicky'),
        ('Jothi','Jothi')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=100)
    deadline = models.DateField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    assign_to = models.CharField(max_length=10,choices=emp)

    def __str__(self):
        return self.task_name
    
class TaskUpdate(models.Model):
    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('ongoing', 'Ongoing'),
        ('dropped', 'Dropped'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    task_status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    remarks = models.TextField(default='')

    def __str__(self):
        return f"{self.task.task_name} - {self.task_status}"


class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
