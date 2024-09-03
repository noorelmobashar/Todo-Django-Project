from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):

    name = models.CharField(max_length=150)
    description = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Task(models.Model):

    CHOICES = [
        ('PENDING', 'PENDING'),
        ('IN PROGRESS', 'IN PROGRESS'),
        ('COMPLETED', 'COMPLETED'),
    ]
    title = models.CharField(max_length=150)
    description = models.TextField(null=True)
    status = models.CharField(max_length=15, choices=CHOICES)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Comment(models.Model):

    comment = models.TextField()
    date = models.DateField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

